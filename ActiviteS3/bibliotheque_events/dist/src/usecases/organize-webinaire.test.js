"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const fixed_id_generator_1 = require("../adapters/fixed-id-generator");
const in_memory_webinaire_repository_1 = require("../adapters/in-memory-webinaire-repository");
const organize_webinaire_1 = require("./organize-webinaire");
describe('Feature: organizing a webinaire', () => {
    let repository;
    let idGenerator;
    let useCase;
    beforeEach(() => {
        repository = new in_memory_webinaire_repository_1.InMemoryWebinaireRepository();
        idGenerator = new fixed_id_generator_1.FixedIDGenerator();
        useCase = new organize_webinaire_1.OrganizeWebinaire(repository, idGenerator);
    });
    describe('Scenario: happy path', () => {
        it('should return the ID', async () => {
            const result = await useCase.execute({
                title: 'My first webinaire',
                seats: 100,
                startDate: new Date('2023-01-10T10:00:00.000Z'),
                endDate: new Date('2023-01-10T11:00:00.000Z'),
            });
            expect(result.id).toEqual('id-1');
        });
        it('should insert the webinaire into the database', async () => {
            await useCase.execute({
                title: 'My first webinaire',
                seats: 100,
                startDate: new Date('2023-01-10T10:00:00.000Z'),
                endDate: new Date('2023-01-10T11:00:00.000Z'),
            });
            expect(repository.database.length).toBe(1);
            const createdWebinaire = repository.database[0];
            expect(createdWebinaire.props).toEqual({
                id: 'id-1',
                title: 'My first webinaire',
                seats: 100,
                startDate: new Date('2023-01-10T10:00:00.000Z'),
                endDate: new Date('2023-01-10T11:00:00.000Z'),
            });
        });
    });
});
//# sourceMappingURL=organize-webinaire.test.js.map