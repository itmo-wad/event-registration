
Menu = {
    setEvents: function() {
        $('.list-group.user >').eq(0).addClass('active');
    },

    setMyProfile: function() {
        $('.list-group.user >').eq(1).addClass('active');
    },

    setAllEvents: function() {
        $('.list-group.admin >').eq(0).addClass('active');
    },

    setAllUsers: function() {
        $('.list-group.admin >').eq(1).addClass('active');
    }
};