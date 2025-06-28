import { FixedIDGenerator, ID } from '../../core/adapters/fixed-id-generator';
import { EventRepositoryMocker } from '../adapters/eventRepositoryMocker';
import { AddNewEvent } from './add-event';

describe('Ajouter un évènement', () => {
  let repository: EventRepositoryMocker;
  let idGenerator: FixedIDGenerator;
  let useCase: AddNewEvent;

  const END_DATE = '2026-02-10T11:00:00.000Z';
  const START_DATE = '2026-01-10T10:00:00.000Z';
  const PARTICIPANTS = 100;
  const TITLE = 'Randonnée dans les gorges du Tarn';

  const RANDO_EVENT = {
    id: ID,
    title: TITLE,
    participants: PARTICIPANTS,
    startDate: new Date(START_DATE),
    endDate: new Date(END_DATE),
  };

  beforeEach(() => {
    repository = new EventRepositoryMocker();
    idGenerator = new FixedIDGenerator();
    useCase = new AddNewEvent(repository, idGenerator);
  });

  describe('Scenario: happy path - cas nominal', () => {
    const RANDO_EVENT_PARAMS = {
      title: TITLE,
      participants: PARTICIPANTS,
      startDate: new Date(START_DATE),
      endDate: new Date(END_DATE),
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
