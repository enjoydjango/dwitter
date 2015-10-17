import re

from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter(name='mention')
@stringfilter
def mention(value):
    return re.sub(r'\@(\w+)', r'<a href="/user/\1/">@\1</a>', value)
    # DRY solution using reverse():
    # from django.core.urlresolvers import reverse
    # return re.sub(r'\@(\w+)', lambda u: r'<a href="%s">@%s</a>' %
    #     (reverse('user-page', args=u.groups()), u.groups()[0]), value)

mention.is_safe = True


@register.inclusion_tag('website/toggle_follow.html', takes_context=True)
def follow_or_unfollow_link(context, user, user2):
    context['is_friend'] = bool(user.following.filter(username=user2.username).count())
    context['target_user'] = user2
    return context
