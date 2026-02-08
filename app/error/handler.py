from flask import render_template

from app.error import bp


@bp.app_errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "error/error.j2",
            error_code=404,
            error_title="Page Not Found",
            error_message="The page you are looking for doesn't exist or has been moved.",
        ),
        404,
    )


@bp.app_errorhandler(413)
def request_entity_too_large(e):
    return (
        render_template(
            "error/error.j2",
            error_code=413,
            error_title="File Too Large",
            error_message="The image you uploaded is too large. Please upload an image smaller than 16MB.",
        ),
        413,
    )


@bp.app_errorhandler(500)
def internal_server_error(e):
    return (
        render_template(
            "error/error.j2",
            error_code=500,
            error_title="Server Error",
            error_message="Something went wrong on our end. Please try again later.",
        ),
        500,
    )


@bp.app_errorhandler(405)
def method_not_allowed(e):
    return (
        render_template(
            "error/error.j2",
            error_code=405,
            error_title="Method Not Allowed",
            error_message="The method is not allowed for the requested URL.",
        ),
        405,
    )
