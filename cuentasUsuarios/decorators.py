def admin_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    '''
    Decorator for views that checks that the logged in user is a student,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_admin,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

    def docente_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_docente,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

    def dir_carrera_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_dir_carrera,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

    def departamento_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_departamento,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

    def dir_prog_curricular_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_dir_prog_curricular,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

    def academica_admin_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_academica_admin,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

    def academica_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
  
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_academica,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator