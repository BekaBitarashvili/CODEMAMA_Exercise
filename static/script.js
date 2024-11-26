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

// task15
document.getElementById('createUserForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const address = document.getElementById('address').value;
    const phone = document.getElementById('phone').value;
    const gender = document.getElementById('gender').value;
    const age = document.getElementById('age').value;
    const dob = document.getElementById('dob').value;
    const job = document.getElementById('job').value;

    const userData = { name, email, address, phone, gender, age, dob, job };

    fetch('/api/users', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData),
    })
    .then(response => response.json())
    .then(data => {
        alert('მომხმარებელი არ შეიქმნა! :)');
        fetchUsers();
    })
    .catch(error => alert('Error creating user: ' + error));
});

function fetchUsers() {
    fetch('/api/users')
        .then(response => response.json())
        .then(data => {
            const userList = document.getElementById('userList');
            userList.innerHTML = '';

            data.forEach((user, index) => {
                const li = document.createElement('li');
                li.textContent = `სახელი: ${user.name}, ელ.ფოსტა: ${user.email}, მისამართი: ${user.address}, მობილური: ${user.phone}, სქესი: ${user.gender}, ასაკი: ${user.age}, დაბ. თარიღი: ${user.dob}, სამსახური: ${user.job} `;


                const deleteButton = document.createElement('button');
                deleteButton.textContent = 'წაშლა';
                deleteButton.onclick = function() { deleteUser(0); };
                li.appendChild(deleteButton);

                userList.appendChild(li);
            });
        })
        .catch(error => console.log('Error fetching users:', error));
}

function deleteUser(id) {
    fetch(`/api/users/${id}`, {
        method: 'DELETE',
    })
    .then(response => response.json())
    .then(data => {
        alert('მომხმარებელი წაიშალა!');
        fetchUsers();
    })
    .catch(error => alert('Error deleting user: ' + error));
}

window.onload = fetchUsers;


