document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.getElementById('contact-form');
    const contactList = document.getElementById('contact');
    const searchInput = document.getElementById('search');
    const themeToggle = document.getElementById('theme-toggle');
    const exportBtn = document.getElementById('export-btn');
    const importFile = document.getElementById('import-file');
    
    // Load existing contacts from local storage
    loadContacts();
    
    // Handle form submission
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const name = document.getElementById('name').value;
        const phone = document.getElementById('phone').value;
        const tags = Array.from(document.getElementById('tags').selectedOptions).map(option => option.value);
        
        addContact(name, phone, tags);
        saveContacts();
        renderContacts();
        contactForm.reset();
    });
    
    // Handle search
    searchInput.addEventListener('input', renderContacts);
    
    // Handle theme toggle
    themeToggle.addEventListener('click', () => {
        document.body.classList.toggle('light-theme');
    });
    
    // Handle export to CSV
    exportBtn.addEventListener('click', () => {
        const contacts = getContacts();
        const csv = Object.entries(contacts).map(([name, { phone, tags }]) => {
            return `${name},${phone},${tags.join('|')}`;
        }).join('\n');
        downloadCSV(csv, 'contacts.csv');
    });
    
    // Handle import from CSV
    importFile.addEventListener('change', (e) => {
        const file = e.target.files[0];
        if (file && file.type === 'text/csv') {
            const reader = new FileReader();
            reader.onload = function(event) {
                const csv = event.target.result;
                const lines = csv.split('\n').filter(line => line.trim() !== '');
                const contacts = {};
                lines.forEach(line => {
                    const [name, phone, tags] = line.split(',');
                    contacts[name] = {
                        phone: phone,
                        tags: tags.split('|')
                    };
                });
                localStorage.setItem('contacts', JSON.stringify(contacts));
                renderContacts();
            };
            reader.readAsText(file);
        } else {
            alert('Please upload a valid CSV file.');
        }
    });
    
    function addContact(name, phone, tags) {
        let contacts = getContacts();
        contacts[name] = { phone, tags };
        localStorage.setItem('contacts', JSON.stringify(contacts));
    }
    
    function saveContacts() {
        let contacts = getContacts();
        localStorage.setItem('contacts', JSON.stringify(contacts));
    }
    
    function getContacts() {
        return JSON.parse(localStorage.getItem('contacts')) || {};
    }
    
    function loadContacts() {
        renderContacts();
    }
    
    function renderContacts() {
        const contacts = getContacts();
        const searchQuery = searchInput.value.toLowerCase();
        contactList.innerHTML = '';
        
        for (const [name, { phone, tags }] of Object.entries(contacts)) {
            if (name.toLowerCase().includes(searchQuery) || phone.includes(searchQuery)) {
                const li = document.createElement('li');
                li.innerHTML = `
                    <strong>${name}</strong>
                    <span>Phone: ${phone}</span>
                    <span>Tags: ${tags.join(', ')}</span>
                    <button onclick="updateContact('${name}')">Update</button>
                    <button onclick="deleteContact('${name}')">Delete</button>
                `;
                contactList.appendChild(li);
            }
        }
    }
    
    window.updateContact = function(name) {
        const contacts = getContacts();
        const contact = contacts[name];
        if (contact) {
            document.getElementById('name').value = name;
            document.getElementById('phone').value = contact.phone;
            document.getElementById('tags').value = contact.tags;
            deleteContact(name); // Remove old contact before updating
        }
    };
    
    window.deleteContact = function(name) {
        let contacts = getContacts();
        delete contacts[name];
        localStorage.setItem('contacts', JSON.stringify(contacts));
        renderContacts();
    };
    
    function downloadCSV(csv, filename) {
        const csvFile = new Blob([csv], { type: 'text/csv' });
        const downloadLink = document.createElement('a');
        downloadLink.download = filename;
        downloadLink.href = window.URL.createObjectURL(csvFile);
        downloadLink.click();
    }
});