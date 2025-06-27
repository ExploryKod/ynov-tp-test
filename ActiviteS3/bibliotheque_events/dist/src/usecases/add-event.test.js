"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const fixed_id_generator_1 = require("../adapters/fixed-id-generator");
const eventRepositoryMocker_1 = require("../adapters/eventRepositoryMocker");
const add_event_1 = require("./add-event");
describe('Ajouter un évènement', () => {
    let repository;
    let idGenerator;
    let useCase;
    beforeEach(() => {
        repository = new eventRepositoryMocker_1.EventRepositoryMocker();
        idGenerator = new fixed_id_generator_1.FixedIDGenerator();
        useCase = new add_event_1.AddNewEvent();
    });
    describe('Scenario: happy path - cas nominal', () => {
        it('Doit insérer un évènement dans la base de donnée', async () => {
            await useCase.execute({
                title: 'Randonnée dans les gorges du Tarn',
                participants: 100,
                startDate: new Date('2026-01-10T10:00:00.000Z'),
                endDate: new Date('2026-01-10T11:00:00.000Z'),
            });
            expect(repository.database.length).toBe(1);
            const createdNewEvent = repository.database[0];
            expect(createdNewEvent.props).toEqual({
                id: 'id-1',
                title: 'Randonnée dans les gorges du Tarn',
                participants: 100,
                startDate: new Date('2026-01-10T10:00:00.000Z'),
                endDate: new Date('2026-01-10T11:00:00.000Z'),
            });
        });
    });
});
//# sourceMappingURL=add-event.test.js.map