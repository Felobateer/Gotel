<script setup>
import navModal from './navModal.vue'
// import logo from '@/assets/Gotel-logo-fedbbdcb.jpg'
const links = [
    { name: 'Home', path: '/' },
    { name: 'About', path: '/about' },
    { name: 'Services', path: '/services' },
    { name: 'Contact', path: '/contact' },
]
</script>

<template>
    <nav class="navbar">
        <div>
            <img  src="../../assets/Gotel-logo-fedbbdcb.jpg" alt="Gotel" class="logo"/>
        </div>
        <navModal :links="links"></navModal>
    </nav>
</template>

<style scoped>
    @import '../../style.css';

    .navbar {
        width: 100%;
        padding: 0 2rem !important;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        background: transparent;
        border-bottom: 1px solid var(--gold);
        overflow-x: hidden;
    }

    .logo {
        width: auto;
        height: 80px;
    }
</style>