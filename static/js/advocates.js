function showAdvInfo(advocate) {
  let div = document.getElementById("myDiv");
  div.innerHTML = `
    <button id="closeButton" style="float: right;">X</button>
    <h1>${advocate.first_name} ${advocate.last_name}</h1>
    <p>Company: ${advocate.company}</p>
    <p>Email: ${advocate.email}</p>
    <p>Industry: ${advocate.industry}</p>
    <p>Company Size: ${advocate.company_size}</p>

    <form method="POST" action="/advocates">
      <label for="prospect_email">Prospect Email</label>
      <input type="text" id="prospect_email" name="prospect_email" required>

      <button type="submit">Submit</button>
    </form>

    <button id="scheduleButton" style="float">Schedule</button>
  `
  ;
  div.style.display = "block";

  document.getElementById("closeButton").addEventListener("click", function() {
    div.style.display = "none";
  });
}


// In this modified code, 
// we've replaced {{ form.prospect_email.label }} with 
// a standard HTML label element, and {{ form.prospect_email() }} 
// with an input field. The name attribute of the input field should 
// match the name of the field in your Flask RequestMeetingForm.
//  You can then use the action and method attributes of the form 
//  element to submit the form to the appropriate Flask endpoint.





  