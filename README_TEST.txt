POLI-ROUTE shell-45｜iPhone実機UI検証専用（2026-10-24）

【変更点】
ルート保存を4ステップに再設計：①行き先 ②経由地（任意） ③道路のコツ（任意） ④確認して保存。
「今日の運転」の操作は変更せず、配色を白・青に統一。
保存済みルートの編集・呼び出し・バックアップ、走行記録などは従来データ構造を維持。

【GitHub Pages更新】
1. 先にテスト版のJSONバックアップをファイルに保存する。
2. ZIPを展開する。
3. GitHub Desktopのpoli-route-device-labのローカルフォルダの中身を、展開した中身で置き換える。'.git'フォルダは削除しない。
4. GitHub DesktopでCommit to main → Push origin。
5. iPhoneのSafari/PWAを開き、変更が見えない場合はSafari再読込・PWA再起動で確認する。

【保存先】
shell-44と同じ検証用キー poli-route-shell44-device-lab-v1 を維持し、既に登録したテストデータを引き継ぐ設計。
後輩専用shell-38の保存キーとデータファイルを含まない。Safariとホーム画面アプリは保存先が異なる場合がある。

【限界】
iPhone実機の永続保存とGoogleマップの実連携は未検証。後輩の実運転には使用しない。
ルートの右左折、通りたい・避けたい道路、時間帯はローカルのメモであり、Googleマップに強制できない。
