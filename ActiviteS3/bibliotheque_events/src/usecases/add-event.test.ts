import { FixedIDGenerator } from '../adapters/fixed-id-generator';
import { EventRepositoryMocker } from '../adapters/eventRepositoryMocker';
import { AddNewEvent } from './add-event';

describe('Ajouter un évènement', () => {
  let repository: EventRepositoryMocker;
  let idGenerator: FixedIDGenerator;
  let useCase: AddNewEvent;

  beforeEach(() => {
    repository = new EventRepositoryMocker();
    idGenerator = new FixedIDGenerator();
    useCase = new AddNewEvent();
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
