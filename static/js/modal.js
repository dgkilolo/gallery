// showModal=(name,desc,url, loc,cat) => {
//   $("#img-label").text(name)
//   $("#myModal").modal("show")
//   $(".modal-title").text(name)
//   $(".mod-img").attr("src",url)
//   $("#img-desc").text(desc)
//   $("#img-loc").text("Location: " + loc)
//   $("#img-cat").text("Category: " + cat)
//   $("#copy-url").val(window.location.origin + url)
// }
showModal=(i_name,url,i_description,location,category) => {
  $("#myModal").modal("show")
  $("#imageName").text(i_name)
  $(".picture").attr("src",url)
  $("#imageDescription").text(i_description)
  $("#imageLocation").text(location)
  $("#imageCategory").text(category)
}