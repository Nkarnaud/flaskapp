from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

#from . import admin
from admin.forms import ProjectForm, RoleForm, UserAssignForm
from .. import db
from ..models import Project, Role, User



def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)


# Project Views


@admin.route('/projects', methods=['GET', 'POST'])
@login_required
def list_projects():
    """
    List all projects
    """
    check_admin()

    projects = Project.query.all()

    return render_template('admin/projects/projects.html', projects=projects, title="Projects")


@admin.route('/projects/add', methods=['GET', 'POST'])
@login_required
def add_project():
    """
    Add a Project to the database
    """
    check_admin()

    add_project = True

    form = ProjectForm()
    if form.validate_on_submit():
        projects = Project(name=form.name.data, description=form.description.data)
        try:
            # add Project to the database
            db.session.add(projects)
            db.session.commit()
            flash('You have successfully added a new Project.')
        except:
            # in case Project name already exists
            flash('Error: Project name already exists.')

        # redirect to projects page
        return redirect(url_for('admin.list_projects'))

    # load Project template
    return render_template('admin/projects/project.html', action="Add", add_project=add_project, form=form, title="Add Project")


@admin.route('/projects/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_project(id):
    """
    Edit a Project
    """
    check_admin()

    add_project = False

    project = Project.query.get_or_404(id)
    form = ProjectForm(obj=project)
    if form.validate_on_submit():
        project.name = form.name.data
        project.description = form.description.data
        db.session.commit()
        flash('You have successfully edited the Project.')

        # redirect to the projects page
        return redirect(url_for('admin.list_projects'))

    form.description.data = project.description
    form.name.data = project.name
    return render_template('admin/projects/project.html', action="Edit",
                           add_project=add_project, form=form,
                           project=project, title="Edit Project")


@admin.route('/projects/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_project(id):
    """
    Delete a Project from the database
    """
    check_admin()

    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    flash('You have successfully deleted the Project.')

    # redirect to the projects page
    return redirect(url_for('admin.list_projects'))

    return render_template(title="Delete Project")



#Role view

@admin.route('/roles')
@login_required
def list_roles():
    check_admin()
    """
    List all roles
    """
    roles = Role.query.all()
    return render_template('admin/roles/roles.html',
                           roles=roles, title='Roles')


@admin.route('/roles/add', methods=['GET', 'POST'])
@login_required
def add_role():
    """
    Add a role to the database
    """
    check_admin()

    add_role = True

    form = RoleForm()
    if form.validate_on_submit():
        role = Role(name=form.name.data,
                    description=form.description.data)

        try:
            # add role to the database
            db.session.add(role)
            db.session.commit()
            flash('You have successfully added a new role.')
        except:
            # in case role name already exists
            flash('Error: role name already exists.')

        # redirect to the roles page
        return redirect(url_for('admin.list_roles'))

    # load role template
    return render_template('admin/roles/role.html', add_role=add_role,
                           form=form, title='Add Role')


@admin.route('/roles/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_role(id):
    """
    Edit a role
    """
    check_admin()

    add_role = False

    role = Role.query.get_or_404(id)
    form = RoleForm(obj=role)
    if form.validate_on_submit():
        role.name = form.name.data
        role.description = form.description.data
        db.session.add(role)
        db.session.commit()
        flash('You have successfully edited the role.')

        # redirect to the roles page
        return redirect(url_for('admin.list_roles'))

    form.description.data = role.description
    form.name.data = role.name
    return render_template('admin/roles/role.html', add_role=add_role,
                           form=form, title="Edit Role")


@admin.route('/roles/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_role(id):
    """
    Delete a role from the database
    """
    check_admin()

    role = Role.query.get_or_404(id)
    db.session.delete(role)
    db.session.commit()
    flash('You have successfully deleted the role.')

    # redirect to the roles page
    return redirect(url_for('admin.list_roles'))

    return render_template(title="Delete Role")


# user view

@admin.route('/users')
@login_required
def list_users():
    """
    List all users
    """
    check_admin()

    users = User.query.all()
    return render_template('admin/users/users.html', users=users, title='Users')


@admin.route('/users/assign/<int:id>', methods=['GET', 'POST'])
@login_required
def assign_user(id):
    """
    Assign a project and a role to an users
    """
    check_admin()

    user = User.query.get_or_404(id)

    # prevent admin from being assigned a project or role
    if user.is_admin:
        abort(403)

    form = UserAssignForm(obj=user)
    if form.validate_on_submit():
        user.project = form.project.data
        user.role = form.role.data
        user.status = form.status.data
        db.session.add(user)
        db.session.commit()
        flash('You have successfully assigned a project and role.')

        # redirect to the roles page
        return redirect(url_for('admin.list_users'))

    return render_template('admin/users/user.html', user=user, form=form, title='Assign User')