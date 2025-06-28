interface IVariables {
  port: number;
  database: string;
  globalPrefix: string;
}

export const variables: IVariables = {
  port: 3000,
  database: process.env.DATABASE_NAME || 'IN-MEMORY-MOCK',
  globalPrefix: process.env.GLOBAL_PREFIX || 'api',
};
