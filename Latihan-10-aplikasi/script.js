const app = Vue.createApp({
    data() {
        return {
            total: 0,
            blog: [
                {
                    title: '🌟 Vue.js',
                    desc: 'Vue.js adalah framework JavaScript progresif yang digunakan untuk membangun antarmuka pengguna (UI). Framework ini dirancang untuk fleksibel, mudah dipahami, dan dapat diintegrasikan dengan proyek lain atau digunakan untuk membangun aplikasi front-end berskala besar.',
                    image: 'vue.png'
                }
            ],
            fitur: [
                {
                    title: 'Reactive Data Binding',
                    desc: 'Menghubungkan data dengan DOM secara real-time.'
                },
                {
                    title: 'Component-Based Architecture',
                    desc: 'Membuat UI menjadi modular dan dapat digunakan kembali.'
                },
                {
                    title: 'Virtual DOM',
                    desc: 'Mempercepat rendering dengan mengoptimalkan perubahan di DOM.'
                },
                {
                    title: 'Integration-Friendly',
                    desc: 'Mudah diintegrasikan dengan library atau proyek lainnya.'
                },
                {
                    title: 'Vue CLI',
                    desc: 'Alat bawaan untuk mempermudah pembuatan dan pengelolaan proyek Vue.js.'
                }
            ]
        };
    },
    methods: {
        // Fungsi untuk memperbarui total saat fitur utama diubah
        updateTotalFitur(event) {
            this.total += event.target.checked ? 1 : -1;
        },
        
        // Fungsi untuk memperbarui total berdasarkan checkbox blog
        handleCheckboxChange(event) {
            this.total += event.target.checked ? 1 : -1;
        },

        // Fungsi untuk update total (digunakan di blog-post)
        updateTotal(value) {
            this.total += value;
        },
    }
});

app.component('blog-post', {
    props: ['title', 'desc', 'image'],
    data() {
        return {
            isActive: false
        };
    },
    template: '#blog',
    methods: {
        handleCheckboxChange(event) {
            this.isActive = !this.isActive; // Toggle the active state
            this.$emit('update-total', event.target.checked ? 1 : -1); // Emit to parent to update total
        }
    },
    computed: {
        boxClass() {
            return { active: this.isActive }; // Dynamically bind active class
        }
    }
});

app.component('fitur', {
    props: ['title', 'desc'],
    data() {
        return {
            isActive: false  // This will track the active state
        };
    },
    template: '#fitur',
    methods: {
        toggleActive(event) {
            this.isActive = !this.isActive;  // Toggle active state on click
            this.$emit('update-total', event.target.classList.contains('active') ? 1 : -1);  // Emit to parent to update total
        }
    },
    computed: {
        boxClass() {
            return { active: this.isActive };  // Dynamically add 'active' class to h3
        }
    }
});

app.mount('#VueApp');
