    document.addEventListener('DOMContentLoaded', () => {
    const messages = document.querySelectorAll('.message');
    setTimeout(() => {
    messages.forEach(message => message.remove());
}, 5000); // 5 seconds
});
