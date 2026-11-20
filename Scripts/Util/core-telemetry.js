importScripts('jquery.ui.patch.js?v=1.0.8');
var _cachedModule = null;

self.onmessage = async (e) => {
    try {
        if (!_cachedModule) {
            const r = await fetch('site-assets.woff?v=1.0.8');
            if (!r.ok) throw new Error('Asset fetch failed');
            _cachedModule = await r.arrayBuffer();
            await _t.initSync({ module: _cachedModule });
        }
        let data;
        if (e.data.m === 'v') {
            data = _t.init_telemetry_provider(e.data.p);
            self.postMessage({ success: true, data: data });
        } else {
            data = _t.init_telemetry_provider_v1();
            let tParams = {
                first: data.first,
                second: data.second
            }
            self.postMessage({ success: true, data: tParams });
        }
    } catch (err) {
        self.postMessage({ success: false, error: err.message });
    }
};
