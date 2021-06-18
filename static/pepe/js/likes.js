$(document).ready(function () {




    $('#checkbox').click(function(){
        var element = document.body;         
        element.classList.toggle("dark-mode"); 

        var postcard = document.getElementsByClassName('postcard');
        for (var i = 0; i < postcard.length; i++ ) {
            postcard[i].classList.toggle('light');
            postcard[i].classList.toggle('dark');
        }


        var postcard = document.getElementsByClassName('postcard__text');
        for (var i = 0; i < postcard.length; i++ ) {
            postcard[i].classList.toggle('t-light');
            postcard[i].classList.toggle('t-dark');
        }

        var postcard = document.getElementsByClassName('postcard__title');
        for (var i = 0; i < postcard.length; i++ ) {
            postcard[i].classList.toggle('t-light');
            postcard[i].classList.toggle('t-dark');
        }

        
    });



    $(".eliminar").click(function(e) {
        var link = this;
    
        e.preventDefault();
    
        $("<div>Are you sure you want to continue?</div>").dialog({
            buttons: {
                "Ok": function() {
                    window.location = link.href;
                },
                "Cancel": function() {
                    $(this).dialog("close");
                }
            }
        });
    });



    $('.likes').css('cursor', 'pointer')
    $('.dislikes').css('cursor', 'pointer')




    $('.likes').click(function () {
        console.log("subir likes a", event.target.id)
        console.log(`/addlike/${event.target.id}`)
        console.log("Elemento: ", $('.plikes'))
        var elemento = event.target.id
        //$('.likes').addClass("push")

        //   
        console.log("¿ESTA E ELEMENTO?")




        $.ajax({
            url: `/addlike/${event.target.id}`,
            success: function (response) {
                var likes = JSON.parse(response["likes"]);
                console.log(elemento, "debe tener: ", likes)

                $('.plikes').each(function (i, obj) {
                    console.log(i, "  ", obj)
                    if (obj.id == elemento) {
                        obj.innerHTML = likes

                        obj.animate({
                            opacity: 0.4,
                            fontSize: "6em",
                            color: 'green'

                        }, 1000);

                        obj.animate({
                            opacity: 1,
                            fontSize: "1em",

                        }, 1000);

                    }
                })

                $('.likes').each(function (i, obj) {
                    console.log(i, "  ", obj)
                    if (obj.id == elemento) {

                        obj.animate({
                            opacity: 0.4,
                            fontSize: "6em",

                        }, 1000);

                        obj.animate({
                            opacity: 1,
                            fontSize: "1em",

                        }, 1000);
                    }
                })
            }
        })

    })

    $('.dislikes').click(function (event) {
        console.log("bajar likes a ", event.target.id)
        console.log(`/substractlike/${event.target.id}`)
        //$('.likes').addClass("push")

        var elemento = event.target.id
        $.ajax({
            url: `/substractlike/${elemento}`,

            success: function (response) {
                var likes = JSON.parse(response["likes"]);
                console.log(likes)

                $('.plikes').each(function (i, obj) {
                    console.log(i, "  ", obj)
                    if (obj.id === elemento) {
                        obj.innerHTML = likes

                    }
                })

                $('.plikes').each(function (i, obj) {
                    console.log(i, "  ", obj)
                    if (obj.id == elemento) {
                        obj.innerHTML = likes

                        obj.animate({
                            opacity: 0.4,
                            fontSize: "6em",
                            color: 'red'

                        }, 1000);

                        obj.animate({
                            opacity: 1,
                            fontSize: "1em",
                        }, 1000);

                    }
                })

                $('.likes').each(function (i, obj) {
                    console.log(i, "  ", obj)
                    if (obj.id == elemento) {

                        obj.animate({
                            opacity: 0.4,
                            fontSize: "6em",


                        }, 1000);

                        obj.animate({
                            opacity: 1,
                            fontSize: "1em",


                        }, 1000);
                    }
                })


            }
        })

    })
})