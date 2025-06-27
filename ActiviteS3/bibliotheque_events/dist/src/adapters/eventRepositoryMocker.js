"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.EventRepositoryMocker = void 0;
class EventRepositoryMocker {
    constructor() {
        this.database = [];
    }
    async create(event) {
        this.database.push(event);
    }
}
exports.EventRepositoryMocker = EventRepositoryMocker;
//# sourceMappingURL=eventRepositoryMocker.js.map