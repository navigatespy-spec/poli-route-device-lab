POLI-ROUTE shell-44｜iPhone実機検証専用（2026-10-23）

【公開禁止データ】
このZIPには後輩向け施設429件・14ルール・30降車メモ等の非公開データを含めていません。
データファイルは公開GitHubへアップロードしないでください。

【試す前に】
1. 専用の空のGitHubリポジトリ（例: poli-route-device-lab）を作成。
2. このZIPのファイルをリポジトリのルートにアップロード（ZIPそのものをアップロードせず展開）。
3. Settings -> Pages -> Deploy from a branch -> main -> /(root) -> Save。
4. HTTPSのGitHub Pages URLが表示されたら、iPhoneのSafariで /device-check.html を開く。
5. device-check.html の手順・チェックリストに沿って実機操作。
6. チェックリスト結果をコピーして開発者へ共有（施設名・住所・実走行情報は含めない）。

注意：manifest・Service Worker は HTTPS（またはlocalhost）でのみ期待どおり動作します。
Safariからのホーム画面追加は、同じ端末でも保存領域が別になる場合があります。
オフラインではGoogleマップが使えません。安全のため実際の運転で試さないでください。
バックアップは「ダウンロード開始」だけでは確認済みにせず、iPhoneのファイルアプリで存在を確認します。
検証版の保存キーは poli-route-shell44-device-lab-v1。後輩用本番・旧検証版とは分離します。
後輩への提供・実走行には使いません。実用化判定は未合格です。
