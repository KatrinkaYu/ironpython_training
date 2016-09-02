
def test_delete_group(app):
    if len(app.group.get_group_list()) == 1:
        app.group.create('group for delete')
    old_list = app.group.get_group_list()
    app.group.delete_first()
    new_list = app.group.get_group_list()
    del old_list[0]
    assert sorted(old_list) == sorted(new_list)



