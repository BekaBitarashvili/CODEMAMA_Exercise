// terminal
const terminal = document.getElementById("terminal-content");

function typeWriter(text, delay) {
    return new Promise((resolve) => {
        let index = 0;
        const interval = setInterval(() => {
            terminal.textContent += text.charAt(index);
            index++;
            if (index > text.length - 1) {
                clearInterval(interval);
                resolve();
            }
        }, delay);
    });
}

async function simulateTyping() {
    await typeWriter("გამარჯობა...\n", 200);
    await typeWriter("თქვენ იმყოფებით ტესტირებისათვის სავარჯიშო ვებ-გვერდზე\n", 100);
    await typeWriter(" \n", 100);
    await typeWriter("თქვენ აქ შეძლებთ ამოხსნათ შემდეგი ამოცანები:\n", 100);
    await typeWriter(">>> მრავალფუნქციური ტესტირება\n", 100);
    await typeWriter(">>> 'იპოვე ყველა შესაძლო ვარიანტი'\n", 100);
    await typeWriter(">>> ლოგიკური პრობლემები\n", 100);
    await typeWriter(">>> მათემატიკური ამოცანები\n", 100);
    await typeWriter(">>> ავტორიზაცია/რეგისტრაცია\n", 100);
    await typeWriter(">>> ტესტ ქეისების შედგენა და ა.შ\n", 100);
    await typeWriter(". . .", 100);
}

simulateTyping();

// delete button logic
