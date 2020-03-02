from telebot.types import Message, CallbackQuery
from .. import Context, State
from app.telegram import bot


class Default(State):
    def handle_text(self, msg: Message) -> None:
        tg_id = msg.from_user.id
        bot.send_start_message(msg)

    def handle_button(self, call) -> None:
        company_id = call.data.split(' ')[1]
        msg_to_del = bot.send_message(call.from_user.id, texts.ask_phone[call.from_user.language_code]).message_id
        self._user.transition_to(FormingOrder(company_id, msg_to_del))

        partner = Partner.query.filter_by(tg_id=call.from_user.id).first()
        partner.state = STATES.FormingOrder
        db.session.commit()


class GetRemind(State):
    def handle_text(self, msg) -> None:
        pass

    def handle_button(self, call) -> None:
        pass
