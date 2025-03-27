class TimeLimitedCache {
    constructor() {
        this.cache = new Map();
    }

    set(key, value, duration) {
        const currentTime = Date.now();
        const exists = this.cache.has(key) && this.cache.get(key).expiry > currentTime;
        this.cache.set(key, { value, expiry: currentTime + duration });
        return exists;
    }

    get(key) {
        const currentTime = Date.now();
        if (this.cache.has(key) && this.cache.get(key).expiry > currentTime) {
            return this.cache.get(key).value;
        }
        return -1;
    }

    count() {
        const currentTime = Date.now();
        let count = 0;
        for (const [key, data] of this.cache) {
            if (data.expiry > currentTime) {
                count++;
            }
        }
        return count;
    }
}
