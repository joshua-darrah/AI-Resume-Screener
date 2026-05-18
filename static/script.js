
/*  Drag & drop  */
function handleDrag(e) {
    e.preventDefault();
    document.getElementById('dropzone').classList.add('drag');
}

function handleDragLeave() {
    document.getElementById('dropzone').classList.remove('drag');
}

function handleDrop(e) {
    e.preventDefault();
    document.getElementById('dropzone').classList.remove('drag');
    const file = e.dataTransfer.files[0];
    if (file) showFile(file);
}

function handleFile(input) {
    if (input.files[0]) showFile(input.files[0]);
}

function showFile(file) {
    document.getElementById('file-name').textContent = file.name;
    document.getElementById('file-size').textContent = (file.size / 1024).toFixed(1) + ' KB';
    document.getElementById('file-selected').classList.add('show');
}

function removeFile() {
    document.querySelector('input[name="resume"]').value = '';
    document.getElementById('file-selected').classList.remove('show');
}

/*  Character counter  */
function updateCharCount() {
    const len = document.querySelector('textarea[name="job_description"]').value.length;
    document.getElementById('char-count').textContent = len.toLocaleString();
}

/*  Analysis mode toggle (UI only)  */
function selectMode(el) {
    document.querySelectorAll('.rs-mode-card').forEach(c => c.classList.remove('active'));
    el.classList.add('active');
}

/*  Clear form  */
function clearForm() {
    removeFile();
    document.querySelector('textarea[name="job_description"]').value = '';
    updateCharCount();
    document.querySelectorAll('.rs-mode-card').forEach((c, i) => {
        c.classList.toggle('active', i === 0);
    });
}

/* Loading spinner on submit (UX only — real POST still fires)  */
function handleSubmitClick() {
    const hasFile = document.querySelector('input[name="resume"]').value;
    const jd = document.querySelector('textarea[name="job_description"]').value.trim();
    if (!hasFile || !jd) return; // let HTML5 validation handle empty fields
    document.getElementById('analyze-btn').classList.add('loading');
}

/*  Animate sidebar meter bars on page load  */
window.addEventListener('load', () => {
    document.querySelectorAll('.rs-bar-fill').forEach(el => {
        const target = el.getAttribute('data-target') + '%';
        el.style.width = '0%';
        setTimeout(() => { el.style.width = target; }, 400);
    });
});