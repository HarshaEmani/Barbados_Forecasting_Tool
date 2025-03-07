<template>
  <Tabs value="0">
    <TabList>
      <Tab value="0">Baseline Forecast with Exog</Tab>
      <Tab value="1">Baseline Forecast without Exog</Tab>
      <Tab value="2">Baseline Naive Forecast</Tab>
      <Tab value="3">Baseline Solar Forecast</Tab>
    </TabList>

    <TabPanels>
      <TabPanel value="0">
        <nuxt-plotly v-if="chartData" :data="exogActualData" :layout="layout" />
      </TabPanel>

      <TabPanel value="1">
        <nuxt-plotly v-if="chartData" :data="noExogActualData" :layout="layout" />
      </TabPanel>

      <TabPanel value="2">
        <nuxt-plotly v-if="chartData" :data="naiveActualData" :layout="layout" />
      </TabPanel>

      <TabPanel value="3">
        <!-- <nuxt-plotly :data="solarDataChart" :layout="layout" /> -->
        <!-- {{ solarDataChart }} -->
      </TabPanel>
    </TabPanels>
  </Tabs>
</template>

<script setup>
import { TabList } from 'primevue';

const props = defineProps({
  feederName: {
    type: String,
    // required: true
  },
  feederFilename: {
    type: String,
    // required: true
  },
  dataType: {
    type: String,
    validator: (value) => ['val', 'test'].includes(value),
    // required: true
  },
  solarCapacity: {
    type: String,
    // required: true
  }
});

const traceConfig = {
  actual: { name: 'Actual', line: { color: 'blue' } },
  naive: { name: 'Preds_Naive', line: { color: 'red' } },
  noExog: { name: 'Preds_No_Exog', line: { color: 'green' } },
  exog: { name: 'Preds_Exog', line: { color: 'black' } }
};

// Data transformation
const transformData = (rawData) => {
  if (!rawData) return null;

  const formatSeries = (series) =>
    Object.entries(series).map(([timestamp, value]) => ({
      x: new Date(Number(timestamp)),
      y: value
    }));

  const transformedData = {
    actual: formatSeries(rawData.Actual),
    naive: formatSeries(rawData.Preds_Naive),
    noExog: formatSeries(rawData.Preds_No_Exog),
    exog: formatSeries(rawData.Preds_Exog)
  }

  return transformedData;
};

// Fetch data
const { data: chartData } = await useAsyncData(
  `forecast-data-${props.feederFilename}-${props.dataType}`,
  async () => {
    const { data } = await useFetch(
      `/Forecasts/2024-07-31/${props.feederFilename}_${props.dataType}_results.json`
    );
    return transformData(data.value);
  },
  { server: false }
);

const transformSolarData = (rawData) => {
  if (!rawData) return null;

  // const formatSeries = (series) =>
  //   Object.entries(series).map(([timestamp, value]) => ({
  //     x: new Date(Number(timestamp)),
  //     y: value
  //   }));

  console.log("Printing raw data: ", rawData.index)

  const forecastData = [...rawData.index].map((timestamp, i) => {
    return {
      timestamp: new Date(timestamp),
      value: rawData.data[i][0],  // Extract value correctly
    };
  });

  console.log("Printing forecast data: ", forecastData)

  return forecastData;

  // const transformedData = {
  //   solar: formatSeries(rawData.data),
  // }

  // return transformedData;
};

const solarData = await useAsyncData(
  `forecast-data-${props.feederName}-solar`,
  async () => {
    const { data } = await useFetch(
      `https://barbados-solar-1.onrender.com/forecasts/solar/day_ahead/${props.feederName}`
    );
    return transformSolarData(data.value)
  },
);



// Plot configurations
const layout = ref({
  title: `Forecast for Feeder ${props.feederName} on ${props.dataType.toUpperCase()} data`,
  xaxis: { title: 'Timestamp' },
  yaxis: { title: 'Value' },
  showlegend: true
});

// Computed plot data
const naiveActualData = computed(() => [
  { ...traceConfig.naive, x: chartData.value?.naive.map(d => d.x), y: chartData.value?.naive.map(d => d.y) },
  { ...traceConfig.actual, x: chartData.value?.actual.map(d => d.x), y: chartData.value?.actual.map(d => d.y) }
]);

const noExogActualData = computed(() => [
  { ...traceConfig.noExog, x: chartData.value?.noExog.map(d => d.x), y: chartData.value?.noExog.map(d => d.y) },
  { ...traceConfig.actual, x: chartData.value?.actual.map(d => d.x), y: chartData.value?.actual.map(d => d.y) }
]);

const exogActualData = computed(() => [
  { ...traceConfig.exog, x: chartData.value?.exog.map(d => d.x), y: chartData.value?.exog.map(d => d.y) },
  { ...traceConfig.actual, x: chartData.value?.actual.map(d => d.x), y: chartData.value?.actual.map(d => d.y) }
]);


const solarDataChart = computed(() => [
  { x: solarData.data.value.map(d => d.timestamp), y: solarData.data.value.map(d => d.value) }

]);

// console.log("Printing solar data: ", solarData.data.value)
// console.log("Printing solar data chart: ", solarDataChart)
console.log("Printing feeder filename: ", props.feederFilename)
</script>