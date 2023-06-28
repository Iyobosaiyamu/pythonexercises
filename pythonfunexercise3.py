import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

class CalculateSales(beam.DoFn):
    def process(self, element):
        if element.startswith('Timestamp'):  # Skip the header row
            return
        timestamp, product_name, quantity, price = element.split(',')
        return [(product_name, (int(quantity), float(price)))]

def calculate_total(element):
    product_name, quantities_prices = element
    total_quantity = sum(q for q, _ in quantities_prices)
    total_price = sum(q * p for q, p in quantities_prices)
    return product_name, (total_quantity, total_price)

def run_pipeline():
    pipeline_options = PipelineOptions()

    with beam.Pipeline(options=pipeline_options) as pipeline:
        data = pipeline | 'ReadFromText' >> beam.io.ReadFromText('sales.csv')

        formatted_data = (
            data
            | 'CalculateSales' >> beam.ParDo(CalculateSales())
            | 'GroupByKey' >> beam.GroupByKey()
            | 'CalculateTotal' >> beam.Map(calculate_total)
            | 'FormatData' >> beam.Map(lambda item: '|'.join([str(x) for x in item]))
        )

        formatted_data | 'WriteToText' >> beam.io.WriteToText('sales_report.psv', file_name_suffix='.psv')

if __name__ == '__main__':
    run_pipeline()
