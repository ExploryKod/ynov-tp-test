import { IIDGenerator } from '../ports/id-generator.interface';

export const ID = 'id-1';

export class FixedIDGenerator implements IIDGenerator {
  generate(): string {
    return ID;
  }
}
