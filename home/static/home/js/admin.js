function openNav() {
    document.getElementById("mySidenav").style.width = "18vw";
    document.getElementById("main").style.marginLeft = "18vw";
    document.getElementById("addbook-wrap").style.borderLeft = "10vw solid #01627f";

  }
  
  function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
    document.getElementById("addbook-wrap").style.borderLeft = "15vw solid #01627f";
  }

  function editBook(book){
    
    document.getElementById("editBookWrap").style.display = "block"
    console.log(book)
  }
  function closeEditBook(){
    document.getElementById("editBookWrap").style.display = "none"
  }
  $( function() {
    $( "#datepicker" ).datepicker({
      dateFormat: "yy-mm-dd"
      ,	duration: "fast"
    });
  } );
  function hideActivity()
  {
    document.getElementById("activityLog").style.display = "none"
  }






/* <table class="table book-table" >
<tr>
    <th>Name</th>
    <th>Auther</th>
    <th>Language</th>
    <th>Publisher</th>
    <th>Publish_date</th>
    <th>Genre</th>
    <th>Action</th>
</tr>
{% for book in books %}
    <tr id = "{{section}}">
        {% if book.image %}
        <td ><span class="book-table-span"><img class="img-fluid book-icon"  src="{{book.image.url}}" alt=""> {{book.name}}</span></td>
        {% else %}
        <td><span class="book-table-span"><img class="img-fluid book-icon" src="{% static 'img/bookplaceholder.png' %}" alt=""> {{book.name}}</span></td>
        {% endif %}
        <td><span class="book-table-span">{{book.auther}}</span></td>
        <td><span class="book-table-span">{{book.language}}</span></td>
        <td><span class="book-table-span">{{book.publisher}}</span></td>
        <td><span class="book-table-span">{{book.publish_date}}</span></td>
        <td><span class="book-table-span">{{book.edition}}</span></td>
        <td><span class="book-table-span"><a href="{% url 'delete-book' book.id %}" id="delete">DELETE</a>&nbsp;|&nbsp;<a  href = "{% url 'edit-book' book.id %}">EDIT</a></span></td>
    </tr>
{% endfor %}
</table>  */
