
def test_add_group(app):
    old_list = app.group.get_group_list()
    app.group.create('test group')
    new_list = app.group.get_group_list()
    old_list.append('test group')
    assert sorted(old_list) == sorted(new_list)


