function checkFlag() {
    const flagInput = document.getElementById('flagInput').value;
    const resultElement = document.getElementById('result');
    
    const correctFlag = "CTF{s1egan0graphy_1ts_c00l}";
    
    if (flagInput === correctFlag) {
        resultElement.textContent = "Correct flag!";
        resultElement.style.color = "green";
    } else {
        resultElement.textContent = "Incorrect flag. Try again.";
        resultElement.style.color = "red";
    }
}
