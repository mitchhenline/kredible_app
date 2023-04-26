function showAdvInfo(advocate) {
    let div = document.getElementById("myDiv");
    div.innerHTML = `
      <button id="closeButton" style="float: right;">X</button>
      <h1>${advocate.first_name} ${advocate.last_name}</h1>
      <p>Company: ${advocate.company}</p>
      <p>Email: ${advocate.email}</p>
      <p>Industry: ${advocate.industry}</p>
      <p>Company Size: ${advocate.company_size}</p>
      <button id="scheduleButton" style="float">Schedule</button>
    `
    ;
    div.style.display = "block";
  
    document.getElementById("closeButton").addEventListener("click", function() {
      div.style.display = "none";
    });
  }
  