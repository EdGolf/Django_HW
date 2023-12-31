import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)


def home(request):
    home_html_text = """
        <a href="/homework1">Главная</a> <a href="/homework1/about">Обо мне</a>
        <h1>Мой сайт</h1>
        <p>С другой стороны дальнейшее развитие различных форм деятельности в значительной степени обуславливает создание форм воздействия! Равным образом консультация с профессионалами из IT обеспечивает широкому кругу специалистов участие в формировании модели развития.

Практический опыт показывает, что рамки и место обучения кадров напрямую зависит от форм воздействия. Задача организации, в особенности же консультация с профессионалами из IT требует от нас анализа всесторонне сбалансированных нововведений! Не следует, однако, забывать о том, что новая модель организационной деятельности представляет собой интересный эксперимент проверки соответствующих условий активизации..</p>
     """
    logger.info("Visited page home")
    return HttpResponse(home_html_text)


def about(request):
    about_html_text = """
        <a href="/homework1">Главная</a> <a href="/homework1/about">Обо мне</a>
        <h1>Обо мне</h1>
        <p>Дорогие друзья, консультация с профессионалами из IT требует от нас системного анализа существующих финансовых и административных условий. Практический опыт показывает, что повышение уровня гражданского сознания в значительной степени обуславливает создание системы масштабного изменения ряда параметров. Таким образом, курс на социально-ориентированный национальный проект влечет за собой процесс внедрения и модернизации системы обучения кадров, соответствующей насущным потребностям.

С другой стороны дальнейшее развитие различных форм деятельности представляет собой интересный эксперимент проверки системы....</p>
    """
    logger.info("Visited page about")
    return HttpResponse(about_html_text)