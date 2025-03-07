<template>
    <div>
        <div style="display: flex; align-items: center;">
            <div style="margin: 15px;">
                <FloatLabel>
                    <Select v-model="selectedFeeder" :options="feeders" optionLabel="label" optionValue="label" placeholder="Select a Feeder" />
                    <label for="over_label">Select a Feeder</label>
                </FloatLabel>
            </div>

            <div style="margin: 15px; ">
                <FloatLabel>
                    <Select v-model="selectedDataType" inputId="over_label" :options="dataTypes" optionLabel="label" optionValue="value" placeholder="Select Data Type" />
                    <label for="over_label">Select Data Type</label>
                </FloatLabel>
            </div>

            <div style="margin-left: auto;">
                <h3 v-if="selectedFeederSolarCapacity && selectedFeeder && selectedDataType">Solar Capacity: {{
                    selectedFeederSolarCapacity }} (kW)</h3>
            </div>
        </div>

        <ForecastCharts v-if="selectedFeeder && selectedDataType" :feeder-name="selectedFeeder" :feeder-filename="selectedFeederFilename" :key="`${selectedFeeder}_${selectedDataType}`" :data-type="selectedDataType" :solar-capacity="selectedFeederSolarCapacity" />

        <!-- {{ dates }} -->
    </div>
</template>

<script setup>
// Parent component (pages/forecasts.vue)

// 
import { ref, } from 'vue';

const dates = ref();


console.log("Selected Dates: ", dates)

// Configure your available feeders
const feeders = ref([
    { label: 'Arch Hall', filename: 'Arch_Hall_ST2B13', solarCapacity: '5594' },
    { label: 'Chapel Street', filename: 'Chapel_Street_TY2B4', solarCapacity: '100' },
    { label: 'Dukes', filename: 'Dukes_ST2B15', solarCapacity: '2409' },
    { label: 'Fontabelle 1', filename: 'Fontabelle_1_TY2B7', solarCapacity: '3099' },
    { label: 'Green Hill', filename: 'Green_Hill_WA2B6', solarCapacity: '7816' },
    { label: 'Hanson (Belmont)', filename: 'Hanson_(Belmont)_BE2B1', solarCapacity: '546' },
    { label: 'Marhill St.', filename: 'Marhill_St._TY2B8', solarCapacity: '208' },
    { label: 'Ometa Mall', filename: 'Ometa_Mall_MA2B4', solarCapacity: '455' },
    { label: 'Sam Lords', filename: 'Sam_Lords_HA2B5', solarCapacity: '4179' },
    { label: 'Sunbury', filename: 'Sunbury_HA2B2', solarCapacity: '4648' },
    { label: 'Swan Street', filename: 'Swan_Street_TY2B6', solarCapacity: '14' },
    { label: 'Welches', filename: 'Welches_WA2B2', solarCapacity: '1211' },
    // Add more feeders as needed
]);

const dataTypes = ref([
    { label: 'Validation Data', value: 'val' },
    { label: 'Test Data', value: 'test' }
]);

const selectedFeeder = ref();
const selectedDataType = ref();

// Compute solar capacity for the selected feeder
const selectedFeederSolarCapacity = computed(() => {
    const feeder = feeders.value.find(f => f.value === selectedFeeder.value);
    return feeder ? feeder.solarCapacity : null;
});

const selectedFeederFilename = computed(() => {
    const feeder = feeders.value.find(f => f.label === selectedFeeder.value);
    return feeder ? feeder.filename : null;
});
</script>