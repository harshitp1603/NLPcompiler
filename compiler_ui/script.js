function sendInstruction() {
  const instruction = document.getElementById('instruction').value;
  const generateBtn = document.querySelector('.generate-btn');
  const codeOutput = document.getElementById('codeOutput');
  const execOutput = document.getElementById('execOutput');

  if (!instruction.trim()) {
    alert('Please enter an instruction');
    return;
  }

  // Update button state
  generateBtn.disabled = true;
  generateBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Generating...';
  
  // Clear previous outputs
  codeOutput.innerText = '';
  execOutput.innerText = '';

  fetch('/compile', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ instruction })
  })
    .then(res => {
      if (!res.ok) {
        throw new Error('Network response was not ok');
      }
      return res.json();
    })
    .then(data => {
      codeOutput.innerText = data.code;
      execOutput.innerText = data.output;
    })
    .catch(err => {
      console.error('Error:', err);
      execOutput.innerText = '❌ An error occurred while processing your request. Please try again.';
    })
    .finally(() => {
      // Reset button state
      generateBtn.disabled = false;
      generateBtn.innerHTML = '<i class="fas fa-magic"></i> Generate Code';
    });
}

function copyCode() {
  const codeOutput = document.getElementById('codeOutput');
  const copyBtn = document.querySelector('.copy-btn');
  
  if (!codeOutput.innerText) {
    return;
  }

  navigator.clipboard.writeText(codeOutput.innerText)
    .then(() => {
      // Visual feedback
      const originalText = copyBtn.innerHTML;
      copyBtn.innerHTML = '<i class="fas fa-check"></i> Copied!';
      copyBtn.style.color = '#22c55e';
      
      setTimeout(() => {
        copyBtn.innerHTML = originalText;
        copyBtn.style.color = '';
      }, 2000);
    })
    .catch(err => {
      console.error('Failed to copy:', err);
      alert('Failed to copy code to clipboard');
    });
}
