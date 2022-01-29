from mtg.ml.utils import load_model
from mtg.ml.display import draft_log_ai
import pickle

draft_model, attrs = load_model("/content/mtg/draft_model.VOW.PremierDraft")
build_model, cards = load_model("/content/mtg/build_model.VOW.PremierDraft", extra_pickle="cards.pkl")
expansion = pickle.load(open("/content/mtg/expansion.VOW.PremierDraft.pkl", "rb"))

log = 'https://www.17lands.com/draft/a7b6f26686734265abee61d95ec08081'
token = '94f22b0985e8440bb6631b7796e555ea'
# log_url[0] will be a link to a 17lands draft log
# log_url[1] will be a link to a sealeddeck.tech deckbuild
log_url = draft_log_ai(
    log,
    draft_model,
    expansion=expansion,
    token=token,
    build_model=build_model,
)

print(log_url[0])
print(log_url[1])
