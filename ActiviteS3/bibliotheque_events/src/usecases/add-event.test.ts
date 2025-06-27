import { FixedIDGenerator } from '../adapters/fixed-id-generator';
import { EventRepositoryMocker } from '../adapters/eventRepositoryMocker';
import { AddNewEvent } from './add-event';

describe('Ajouter un évènement', () => {
  let repository: EventRepositoryMocker;
  let idGenerator: FixedIDGenerator;
  let useCase: AddNewEvent;

  const ID = 'id-1';

  const RANDO_EVENT = {
    id: ID,
    title: 'Randonnée dans les gorges du Tarn',
    participants: 100,
    startDate: new Date('2026-01-10T10:00:00.000Z'),
    endDate: new Date('2026-01-10T11:00:00.000Z'),
  };

  beforeEach(() => {
    repository = new EventRepositoryMocker();
    idGenerator = new FixedIDGenerator();
    useCase = new AddNewEvent(repository, idGenerator);
  });

  describe('Scenario: happy path - cas nominal', () => {
    const RANDO_EVENT_PARAMS = {
      title: 'Randonnée dans les gorges du Tarn',
      participants: 100,
      startDate: new Date('2026-01-10T10:00:00.000Z'),
      endDate: new Date('2026-01-10T11:00:00.000Z'),
    };

    it("Doit retourner un id de l'évènement", async () => {
      const result = await useCase.execute(RANDO_EVENT_PARAMS);

      expect(result.id).toEqual(ID);
    });

    it('Doit insérer un évènement dans la base de donnée', async () => {
      await useCase.execute(RANDO_EVENT_PARAMS);

      expect(repository.database.length).toBe(1);

      const createdNewEvent = repository.database[0];
      expect(createdNewEvent.props).toEqual(RANDO_EVENT);
    });
  });
});
