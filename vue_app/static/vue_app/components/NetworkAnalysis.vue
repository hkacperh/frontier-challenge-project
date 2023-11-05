<!-- NetworkAnalysis.vue -->
<template>
    <div class="network-analysis">
        <h1 class="page-title">Network Failure Prediction Analysis</h1>
        <div class="statistics">
            <div class="category">
                <h2>No risk of failure</h2>
                <p>{{ statistics.no_risk }}</p>
            </div>
            <div class="category">
                <h2>Risk of failure</h2>
                <p>{{ statistics.risk }}</p>
            </div>
            <div class="category">
                <h2>Risk confirmed</h2>
                <p>{{ statistics.risk_confirmed }}</p>
            </div>
        </div>
        <div class="chart"></div>
        <div class="network-lists">
            <div class="list">
                <h2>Risk of Failure</h2>
                <ul>
                    <li v-for="network in riskList" :key="network">{{ network }}</li>
                </ul>
            </div>
            <div class="list">
                <h2>Risk Confirmed</h2>
                <ul>
                    <li v-for="network in confirmedList" :key="network">{{ network }}</li>
                </ul>
            </div>
        </div>
    </div>
</template>
  
<script>

import axios from 'axios';

export default {
    data() {
        return {
            statistics: {},
            riskList: [],
            confirmedList: [],
        };
    },
    mounted() {
        // Fetch data from your Django API endpoints
        this.fetchNetworkStatistics();
        this.fetchNetworkLists();
    },
    methods: {
        fetchNetworkStatistics() {
            // Make an API call to get network statistics
            axios.get('/backend/get_network_statistics/')
                .then((response) => {
                    // Handle the API response here
                    this.statistics = response.data;
                })
                .catch((error) => {
                    // Handle errors, e.g., show an error message
                    console.error('Error fetching network statistics:', error);
                });
        },
        fetchNetworkLists() {
            // Make an API call to get network lists
            axios.get('/backend/get_network_lists/')
                .then((response) => {
                    // Handle the API response here
                    this.riskList = response.data.risk_list;
                    this.confirmedList = response.data.confirmed_list;
                })
                .catch((error) => {
                    // Handle errors, e.g., show an error message
                    console.error('Error fetching network lists:', error);
                });
        },
    },
};
</script>
  
<style scoped>
/* Add your CSS for styling here */
.network-analysis {
    /* Your styles for the entire page */
}

.page-title {
    /* Your styles for the page title */
}

.statistics {
    /* Your styles for statistics */
}

.category {
    /* Your styles for each category in statistics */
}

.chart {
    /* Your styles for the chart */
}

.network-lists {
    /* Your styles for network lists */
}

.list {
    /* Your styles for each list */
}

ul {
    /* Your styles for list items */
}
</style>
  