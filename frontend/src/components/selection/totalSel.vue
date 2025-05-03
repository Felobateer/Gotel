<script>
    import { primarySel} from './primarySel.vue'
    import { secondarySel} from './secondarySel.vue'
</script>

<template>
    <div class="totalSel">
        <primarySel/>
        <secondarySel/>
    </div>
</template>

<style scoped>
    .totalSel {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 20px;
        background-color: #f0f0f0;
        border-radius: 8px;
    }
    .totalSel h1 {
        font-size: 24px;
        margin-bottom: 20px;
    }
    .totalSel p {
        font-size: 16px;
        color: #555;
    }
</style>