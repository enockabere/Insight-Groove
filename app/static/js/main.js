$(document).ready(function(){
    $("#comm").click(function(event){
        event.preventDefault();
        $("#myform").toggle(500)
    })
})
// $(document).ready(function(){
//     $("#l1").click(function(event){
//         event.preventDefault();
//         $("#love").show()
//         $("#positive").hide(500)
//         $("#meme").hide(500)
//         $("#fam").hide(500)
//     })
// })
// $(document).ready(function(){
//     $("#l2").click(function(event){
//         event.preventDefault();
//         $("#positive").show()
//         $("#love").hide(500)
//         $("#meme").hide(500)
//         $("#fam").hide(500)
//     })
// })
// $(document).ready(function(){
//     $("#l3").click(function(event){
//         event.preventDefault();
//         $("#meme").show()
//         $("#positive").hide(500)
//         $("#love").hide(500)
//         $("#fam").hide(500)
//     })
// })
// $(document).ready(function(){
//     $("#l4").click(function(event){
//         event.preventDefault();
//         $("#fam").show()
//         $("#meme").hide(500)
//         $("#positive").hide(500)
//         $("#love").hide(500)
//     })
// })
// $(document).ready(function(){
//     $("#l5").click(function(event){
//         event.preventDefault();
//         $("#fam").show(500)
//         $("#meme").show(500)
//         $("#positive").show(500)
//         $("#love").show(500)
//     })
// })
function deletePitch(pitchId){
    fetch('/delete-pitch',{
        method:'POST',
        body: JSON.stringify({pitchId: pitchId})
    }).then ((_res) => {
        window.location.href = "/profile";
    })
}

$(function () {
     $(".like").click(function () {
         var input = $(this).find('.qty1');
         input.val(parseInt(input.val())+ 1);
     });

     $(".dislike").click(function () {
         var input = $(this).find('.qty2');
         input.val(input.val() - 1);
     });
});

$(document).ready(function() {

    // Hide the div
    $(".alert").hide();

    // Show the div in 5s
    $(".alert").delay(3000).fadeIn(1000);

});