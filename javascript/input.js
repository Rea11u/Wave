function checkFlag() {
    const flagInput = document.getElementById('flagInput').value;
    const resultElement = document.getElementById('result');
    
    const correctFlag = "CTF{this_is_a_super_secret_flag}";
    
    if (flagInput === correctFlag) {
        resultElement.textContent = "Correct flag!";
        resultElement.style.color = "green";
    } else {
        resultElement.textContent = "Incorrect flag. Try again.";
        resultElement.style.color = "red";
    }
}
