import json
import os
from pathlib import Path

# Translation data for all 24 languages
PROMO_STRINGS = {
    "en": {
        "ChannelPromoTitle": "GummyGram Fork",
        "ChannelPromoText": "Subscribe to our official Telegram channel for updates and announcements!",
        "ChannelPromoSubscribe": "Subscribe",
        "ChannelPromoLater": "Later",
    },
    "ru": {
        "ChannelPromoTitle": "GummyGram Fork",
        "ChannelPromoText": "Подпишитесь на наш официальный Telegram-канал, чтобы быть в курсе новостей и обновлений!",
        "ChannelPromoSubscribe": "Подписаться",
        "ChannelPromoLater": "Позже",
    },
    "uk": {
        "ChannelPromoTitle": "GummyGram Fork",
        "ChannelPromoText": "Підпишіться на наш офіційний Telegram-канал, щоб бути в курсі новин та оновлень!",
        "ChannelPromoSubscribe": "Підписатися",
        "ChannelPromoLater": "Пізніше",
    },
    "be": {
        "ChannelPromoTitle": "GummyGram Fork",
        "ChannelPromoText": "Падпішыцеся на наш афіцыйны Telegram-канал, каб быць у курсе навін і абнаўленняў!",
        "ChannelPromoSubscribe": "Падпісацца",
        "ChannelPromoLater": "Пазней",
    },
    "de": {
        "ChannelPromoTitle": "GummyGram Fork",
        "ChannelPromoText": "Abonnieren Sie unseren offiziellen Telegram-Kanal für Neuigkeiten und Updates!",
        "ChannelPromoSubscribe": "Abonnieren",
        "ChannelPromoLater": "Später",
    },
    "es": {
        "ChannelPromoTitle": "GummyGram Fork",
        "ChannelPromoText": "¡Suscríbete a nuestro canal oficial de Telegram para recibir noticias y actualizaciones!",
        "ChannelPromoSubscribe": "Suscribirse",
        "ChannelPromoLater": "Más tarde",
    },
    "fr": {
        "ChannelPromoTitle": "GummyGram Fork",
        "ChannelPromoText": "Abonnez-vous à notre canal Telegram officiel pour suivre les actualités et mises à jour !",
        "ChannelPromoSubscribe": "S'abonner",
        "ChannelPromoLater": "Plus tard",
    },
    "it": {
        "ChannelPromoTitle": "GummyGram Fork",
        "ChannelPromoText": "Iscriviti al nostro canale Telegram ufficiale per aggiornamenti e novità!",
        "ChannelPromoSubscribe": "Iscriviti",
        "ChannelPromoLater": "Più tardi",
    },
    "pt": {
        "ChannelPromoTitle": "GummyGram Fork",
        "ChannelPromoText": "Inscreva-se no nosso canal oficial do Telegram para notícias e atualizações!",
        "ChannelPromoSubscribe": "Inscrever-se",
        "ChannelPromoLater": "Mais tarde",
    },
    "pl": {
        "ChannelPromoTitle": "GummyGram Fork",
        "ChannelPromoText": "Subskrybuj nasz oficjalny kanał na Telegramie, aby być na bieżąco z aktualizacjami!",
        "ChannelPromoSubscribe": "Subskrybuj",
        "ChannelPromoLater": "Później",
    },
    "tr": {
        "ChannelPromoTitle": "GummyGram Fork",
        "ChannelPromoText": "Haberler ve güncellemeler için resmi Telegram kanalımıza abone olun!",
        "ChannelPromoSubscribe": "Abone Ol",
        "ChannelPromoLater": "Daha Sonra",
    },
    "ar": {
        "ChannelPromoTitle": "GummyGram Fork",
        "ChannelPromoText": "اشترك في قناتنا الرسمية على تيليجرام للحصول على آخر الأخبار والتحديثات!",
        "ChannelPromoSubscribe": "اشتراك",
        "ChannelPromoLater": "لاحقاً",
    },
    "fa": {
        "ChannelPromoTitle": "GummyGram Fork",
        "ChannelPromoText": "برای اطلاع از اخبار و بهروزرسانیها در کانال رسمی تلگرام ما عضو شوید!",
        "ChannelPromoSubscribe": "عضویت",
        "ChannelPromoLater": "بعداً",
    },
    "he": {
        "ChannelPromoTitle": "GummyGram Fork",
        "ChannelPromoText": "הירשם לערוץ הטלגרם הרשמי שלנו לעדכונים וחדשות!",
        "ChannelPromoSubscribe": "הירשם",
        "ChannelPromoLater": "מאוחר יותר",
    },
    "el": {
        "ChannelPromoTitle": "GummyGram Fork",
        "ChannelPromoText": "Εγγραφείτε στο επίσημο κανάλι μας στο Telegram για νέα και ενημερώσεις!",
        "ChannelPromoSubscribe": "Εγγραφή",
        "ChannelPromoLater": "Αργότερα",
    },
    "ro": {
        "ChannelPromoTitle": "GummyGram Fork",
        "ChannelPromoText": "Abonează-te la canalul nostru oficial de Telegram pentru noutăți și actualizări!",
        "ChannelPromoSubscribe": "Abonează-te",
        "ChannelPromoLater": "Mai târziu",
    },
    "fi": {
        "ChannelPromoTitle": "GummyGram Fork",
        "ChannelPromoText": "Tilaa virallinen Telegram-kanavamme pysyäksesi ajan tasalla uutisista ja päivityksistä!",
        "ChannelPromoSubscribe": "Tilaa",
        "ChannelPromoLater": "Myöhemmin",
    },
    "lv": {
        "ChannelPromoTitle": "GummyGram Fork",
        "ChannelPromoText": "Abonējiet mūsu oficiālo Telegram kanālu jaunumiem un atjauninājumiem!",
        "ChannelPromoSubscribe": "Abonēt",
        "ChannelPromoLater": "Vēlāk",
    },
    "vi": {
        "ChannelPromoTitle": "GummyGram Fork",
        "ChannelPromoText": "Đăng ký kênh Telegram chính thức của chúng tôi để cập nhật tin tức và thông báo mới nhất!",
        "ChannelPromoSubscribe": "Đăng ký",
        "ChannelPromoLater": "Để sau",
    },
    "zh": {
        "ChannelPromoTitle": "GummyGram Fork",
        "ChannelPromoText": "订阅我们的 Telegram 官方频道以获取最新消息和更新！",
        "ChannelPromoSubscribe": "订阅",
        "ChannelPromoLater": "稍后",
    },
    "zh-hans": {
        "ChannelPromoTitle": "GummyGram Fork",
        "ChannelPromoText": "订阅我们的 Telegram 官方频道以获取最新消息和更新！",
        "ChannelPromoSubscribe": "订阅",
        "ChannelPromoLater": "稍后",
    },
    "zh-hant": {
        "ChannelPromoTitle": "GummyGram Fork",
        "ChannelPromoText": "訂閱我們的 Telegram 官方頻道以獲取最新消息和更新！",
        "ChannelPromoSubscribe": "訂閱",
        "ChannelPromoLater": "稍後",
    },
    "eo": {
        "ChannelPromoTitle": "GummyGram Fork",
        "ChannelPromoText": "Abonu nian oficialan Telegram-kanalon por novaĵoj kaj ĝisdatigoj!",
        "ChannelPromoSubscribe": "Aboni",
        "ChannelPromoLater": "Poste",
    },
    "os": {
        "ChannelPromoTitle": "GummyGram Fork",
        "ChannelPromoText": "Бафыссут нæ официалон Telegram-каналмæ, цæмæй ног хабæрттæй хабардар уат!",
        "ChannelPromoSubscribe": "Бафыссын",
        "ChannelPromoLater": "Фæстæдæр",
    },
}

BLOCKED_AVATARS_STRINGS = {
    "en": {
        "LoadBlockedAvatars": "Load Avatars of Blocked Users",
        "LoadBlockedAvatarsDescription": "Allows you to see profile pictures of users who blocked you, if they have a public username.",
    },
    "ru": {
        "LoadBlockedAvatars": "Загружать аватарки заблокированных пользователей",
        "LoadBlockedAvatarsDescription": "Позволяет видеть аватарки пользователей, которые вас заблокировали (при наличии у них юзернейма).",
    },
    "uk": {
        "LoadBlockedAvatars": "Завантажувати аватарки заблокованих користувачів",
        "LoadBlockedAvatarsDescription": "Дозволяє бачити аватарки користувачів, які вас заблокували (за наявності у них юзернейма).",
    },
    "be": {
        "LoadBlockedAvatars": "Загружаць аватаркі заблакаваных карыстальнікаў",
        "LoadBlockedAvatarsDescription": "Дазваляе бачыць аватаркі карыстальнікаў, якія вас заблакавалі (пры наяўнасці ў іх юзернэйма).",
    },
    "de": {
        "LoadBlockedAvatars": "Profilbilder von blockierten Benutzern laden",
        "LoadBlockedAvatarsDescription": "Ermöglicht das Anzeigen von Profilbildern von Benutzern, die Sie blockiert haben, sofern sie einen Benutzernamen haben.",
    },
    "es": {
        "LoadBlockedAvatars": "Cargar fotos de perfil de usuarios bloqueados",
        "LoadBlockedAvatarsDescription": "Permite ver las fotos de perfil de usuarios que te han bloqueado si tienen un nombre de usuario público.",
    },
    "fr": {
        "LoadBlockedAvatars": "Charger les photos de profil des utilisateurs bloqués",
        "LoadBlockedAvatarsDescription": "Permet d'afficher les photos de profil des utilisateurs qui vous ont bloqué, s'ils ont un nom d'utilisateur public.",
    },
    "it": {
        "LoadBlockedAvatars": "Carica foto profilo degli utenti bloccati",
        "LoadBlockedAvatarsDescription": "Consente di vedere le foto profilo degli utenti che ti hanno bloccato, se hanno un nome utente pubblico.",
    },
    "pt": {
        "LoadBlockedAvatars": "Carregar fotos de perfil de usuários bloqueados",
        "LoadBlockedAvatarsDescription": "Permite ver fotos de perfil de usuários que bloquearam você, se eles tiverem um nome de usuário público.",
    },
    "pl": {
        "LoadBlockedAvatars": "Wczytuj awatary zablokowanych użytkowników",
        "LoadBlockedAvatarsDescription": "Pozwala zobaczyć zdjęcia profilowe użytkowników, którzy cię zablokowali, jeśli mają nazwę użytkownika.",
    },
    "tr": {
        "LoadBlockedAvatars": "Engellenen kullanıcıların profil resimlerini yükle",
        "LoadBlockedAvatarsDescription": "Kullanıcı adı olan ve sizi engelleyen kullanıcıların profil resimlerini görmenizi sağlar.",
    },
    "ar": {
        "LoadBlockedAvatars": "تحميل الصور الشخصية للمستخدمين المحظورين",
        "LoadBlockedAvatarsDescription": "يتيح لك رؤية الصور الشخصية للمستخدمين الذين قاموا بحظرك، إذا كان لديهم اسم مستخدم عام.",
    },
    "fa": {
        "LoadBlockedAvatars": "بارگیری عکس‌های پروفایل کاربران مسدود شده",
        "LoadBlockedAvatarsDescription": "به شما امکان می‌دهد عکس‌های پروفایل کاربرانی که شما را مسدود کرده‌اند را در صورت داشتن نام کاربری عمومی مشاهده کنید.",
    },
    "he": {
        "LoadBlockedAvatars": "טען תמונות פרופיל של משתמשים חסומים",
        "LoadBlockedAvatarsDescription": "מאפשר לראות תמונות פרופיל של משתמשים שחסמו אותך, אם יש להם שם משתמש ציבורי.",
    },
    "el": {
        "LoadBlockedAvatars": "Φόρτωση εικόνων προφίλ αποκλεισμένων χρηστών",
        "LoadBlockedAvatarsDescription": "Σας επιτρέπει να βλέπετε τις εικόνες προφίλ χρηστών που σας έχουν αποκλείσει, εάν έχουν δημόσιο όνομα χρήστη.",
    },
    "ro": {
        "LoadBlockedAvatars": "Încarcă imaginile de profil ale utilizatorilor blocați",
        "LoadBlockedAvatarsDescription": "Permite vizualizarea imaginilor de profil ale utilizatorilor care te-au blocat, dacă au un nume de utilizator public.",
    },
    "fi": {
        "LoadBlockedAvatars": "Lataa estettyjen käyttäjien profiilikuvat",
        "LoadBlockedAvatarsDescription": "Näyttää sinut estäneiden käyttäjien profiilikuvat, jos heillä on julkinen käyttäjänimi.",
    },
    "lv": {
        "LoadBlockedAvatars": "Ielādēt bloķēto lietotāju profila attēlus",
        "LoadBlockedAvatarsDescription": "Ļauj redzēt to lietotāju profila attēlus, kuri jūs bloķējuši, ja viņiem ir publisks lietotājvārds.",
    },
    "vi": {
        "LoadBlockedAvatars": "Tải ảnh đại diện của người dùng bị chặn",
        "LoadBlockedAvatarsDescription": "Cho phép bạn xem ảnh đại diện của người dùng đã chặn bạn nếu họ có tên người dùng công khai.",
    },
    "zh": {
        "LoadBlockedAvatars": "加载已拉黑用户的头像",
        "LoadBlockedAvatarsDescription": "允许您查看拉黑您的用户的个人资料照片（如果他们有公开用户名）。",
    },
    "zh-hans": {
        "LoadBlockedAvatars": "加载已拉黑用户的头像",
        "LoadBlockedAvatarsDescription": "允许您查看拉黑您的用户的个人资料照片（如果他们有公开用户名）。",
    },
    "zh-hant": {
        "LoadBlockedAvatars": "載入已封鎖使用者的頭像",
        "LoadBlockedAvatarsDescription": "允許您查看封鎖您的使用者的個人資料照片（如果他們有公開使用者名稱）。",
    },
    "eo": {
        "LoadBlockedAvatars": "Ŝargi profilbildojn de blokitaj uzantoj",
        "LoadBlockedAvatarsDescription": "Ebligas vidi profilbildojn de uzantoj, kiuj blokis vin, se ili havas publikan uzantnomon.",
    },
    "os": {
        "LoadBlockedAvatars": "Сæхгæд пайдагæнджыты аватаркæтæ æвгæнын",
        "LoadBlockedAvatarsDescription": "Дæтты бар уынын уыцы пайдагæнджыты аватаркæтæ, кæцытæ дæ сæхгæдтой (кæд сæм ис юзернейм).",
    },
}

def main():
    repo_root = Path(__file__).resolve().parent.parent
    langs_dir = repo_root / "values" / "langs"
    
    all_lang_dirs = sorted([d.name for d in langs_dir.iterdir() if d.is_dir()])
    print(f"Found {len(all_lang_dirs)} language directories: {all_lang_dirs}")
    assert len(all_lang_dirs) == 24, f"Expected 24 language directories, got {len(all_lang_dirs)}"
    
    modified_files = []
    
    for lang in all_lang_dirs:
        shared_json_path = langs_dir / lang / "Shared.json"
        assert shared_json_path.exists(), f"File does not exist: {shared_json_path}"
        
        with open(shared_json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        # 1. Add / update blocked avatars keys
        assert lang in BLOCKED_AVATARS_STRINGS, f"Missing blocked avatar translations for {lang}"
        data["LoadBlockedAvatars"] = BLOCKED_AVATARS_STRINGS[lang]["LoadBlockedAvatars"]
        data["LoadBlockedAvatarsDescription"] = BLOCKED_AVATARS_STRINGS[lang]["LoadBlockedAvatarsDescription"]
            
        # 2. Add channel promo keys for all languages
        assert lang in PROMO_STRINGS, f"Missing promo translations for {lang}"
        data["ChannelPromoTitle"] = PROMO_STRINGS[lang]["ChannelPromoTitle"]
        data["ChannelPromoText"] = PROMO_STRINGS[lang]["ChannelPromoText"]
        data["ChannelPromoSubscribe"] = PROMO_STRINGS[lang]["ChannelPromoSubscribe"]
        data["ChannelPromoLater"] = PROMO_STRINGS[lang]["ChannelPromoLater"]
        
        # Write back safely with 2 spaces indent and UTF-8 encoding
        output_str = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
        with open(shared_json_path, "w", encoding="utf-8") as f:
            f.write(output_str)
            
        modified_files.append(shared_json_path)
        print(f"Updated: {lang}/Shared.json")
        
    print(f"\nSuccessfully updated {len(modified_files)} files.")
    
    # Verification pass
    print("\n--- Running verification ---")
    expected_keys = [
        "LoadBlockedAvatars",
        "LoadBlockedAvatarsDescription",
        "ChannelPromoTitle",
        "ChannelPromoText",
        "ChannelPromoSubscribe",
        "ChannelPromoLater",
    ]
    
    verified_count = 0
    for lang in all_lang_dirs:
        shared_json_path = langs_dir / lang / "Shared.json"
        with open(shared_json_path, "r", encoding="utf-8") as f:
            verified_data = json.load(f)
            
        for key in expected_keys:
            assert key in verified_data, f"Missing key {key} in {lang}/Shared.json"
            assert isinstance(verified_data[key], str) and len(verified_data[key]) > 0, f"Empty or non-string key {key} in {lang}/Shared.json"
            
        verified_count += 1
        
    print(f"Verification passed: All {verified_count} JSON files parse without errors and contain all expected keys.")

if __name__ == "__main__":
    main()
