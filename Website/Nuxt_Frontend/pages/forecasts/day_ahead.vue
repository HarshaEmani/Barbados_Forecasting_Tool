<template>
    <div class="card flex justify-center">
        <h1>Day Ahead Forecasts</h1>
        <CascadeSelect v-model="selectedCity" :options="countries" optionLabel="cname" optionGroupLabel="name"
            :optionGroupChildren="['states', 'cities']" class="w-56" placeholder="Select a City">
            <template #option="slotProps">
                <div class="flex items-center">
                    <img v-if="slotProps.option.states" :alt="slotProps.option.name"
                        src="https://primefaces.org/cdn/primevue/images/flag/flag_placeholder.png"
                        :class="`flag flag-${slotProps.option.code.toLowerCase()} mr-2`" style="width: 18px" />
                    <i v-if="slotProps.option.cities" class="pi pi-compass mr-2"></i>
                    <i v-if="slotProps.option.cname" class="pi pi-map-marker mr-2"></i>
                    <span>{{ slotProps.option.cname || slotProps.option.name }}</span>
                </div>
            </template>
            <template #dropdownicon>
                <i class="pi pi-map" />
            </template>
            <template #header>
                <div class="font-medium px-3 py-2">Available Countries</div>
            </template>
            <template #footer>
                <div class="px-3 py-1">
                    <Button label="Add New" fluid severity="secondary" text size="small" icon="pi pi-plus" />
                </div>
            </template>
        </CascadeSelect>
    </div>

    <Tabs value="0">
        <TabList>
            <Tab value="0">Probablistic Forecast</Tab>
            <Tab value="1">Baseline Forecast without Exog</Tab>
            <Tab value="2">Baseline Forecast with Exog</Tab>
        </TabList>
        <TabPanels>
            <TabPanel value="0">
                <client-only>
                    <nuxt-plotly :data="lineChart.data" :config="lineChart.config" style="width: 100%"></nuxt-plotly>
                    <nuxt-plotly :data="lineChart.data" :config="lineChart.config" style="width: 100%"></nuxt-plotly>
                </client-only>
            </TabPanel>
            <TabPanel value="1">
                <client-only>
                    <nuxt-plotly :data="lineChart.data" :config="lineChart.config" style="width: 100%"></nuxt-plotly>
                    <nuxt-plotly :data="lineChart.data" :config="lineChart.config" style="width: 100%"></nuxt-plotly>
                </client-only>
            </TabPanel>
            <TabPanel value="2">
                <client-only>
                    <nuxt-plotly :data="lineChart.data" :config="lineChart.config" style="width: 100%"></nuxt-plotly>
                    <nuxt-plotly :data="lineChart.data" :config="lineChart.config" style="width: 100%"></nuxt-plotly>
                </client-only>
            </TabPanel>
        </TabPanels>
    </Tabs>
</template>

<script setup>
import { ref, reactive } from "vue";

const getLinePlotFromData = () => reactive()

let getRandomData = () => {
    return Array.from({ length: 10 }, () => Math.floor(Math.random() * 100));
}

const randomData = getRandomData()

const lineChartData = [{
    x: Array.from({ length: 10 }, (_, i) => i + 1), // X-axis: 1 to 10
    y: getRandomData(), // Y-axis: random values
    type: "line",
    mode: "lines+markers",
    // marker: { color: "blue" },
    // line: { color: "red" },
},
{
    x: Array.from({ length: 10 }, (_, i) => i + 1), // X-axis: 1 to 10
    y: getRandomData(), // Y-axis: random values
    type: "line",
    mode: "lines+markers",
    // marker: { color: "blue" },
    // line: { color: "red" },
}]

const config0 = { scrollZoom: true, displayModeBar: true };


const lineChart = reactive({
    // changeDataNo: 1,
    data: lineChartData,
    // changeConfigNo: 1,
    config: config0,
    // changeLayoutNo: 1,
    // layout: layout0,
});

const selectedCity = ref();
const countries = ref([
    {
        name: 'Australia',
        code: 'AU',
        states: [
            {
                name: 'New South Wales',
                cities: [
                    { cname: 'Sydney', code: 'A-SY' },
                    { cname: 'Newcastle', code: 'A-NE' },
                    { cname: 'Wollongong', code: 'A-WO' }
                ]
            },
            {
                name: 'Queensland',
                cities: [
                    { cname: 'Brisbane', code: 'A-BR' },
                    { cname: 'Townsville', code: 'A-TO' }
                ]
            }
        ]
    },
    {
        name: 'Canada',
        code: 'CA',
        states: [
            {
                name: 'Quebec',
                cities: [
                    { cname: 'Montreal', code: 'C-MO' },
                    { cname: 'Quebec City', code: 'C-QU' }
                ]
            },
            {
                name: 'Ontario',
                cities: [
                    { cname: 'Ottawa', code: 'C-OT' },
                    { cname: 'Toronto', code: 'C-TO' }
                ]
            }
        ]
    },
    {
        name: 'United States',
        code: 'US',
        states: [
            {
                name: 'California',
                cities: [
                    { cname: 'Los Angeles', code: 'US-LA' },
                    { cname: 'San Diego', code: 'US-SD' },
                    { cname: 'San Francisco', code: 'US-SF' }
                ]
            },
            {
                name: 'Florida',
                cities: [
                    { cname: 'Jacksonville', code: 'US-JA' },
                    { cname: 'Miami', code: 'US-MI' },
                    { cname: 'Tampa', code: 'US-TA' },
                    { cname: 'Orlando', code: 'US-OR' }
                ]
            },
            {
                name: 'Texas',
                cities: [
                    { cname: 'Austin', code: 'US-AU' },
                    { cname: 'Dallas', code: 'US-DA' },
                    { cname: 'Houston', code: 'US-HO' }
                ]
            }
        ]
    }
]);
</script>
