---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: U.S. bank
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bank that is licensed to conduct business in the United States
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: As defined in the Federal Deposit Insurance Act, https://www.fdic.gov/regulations/laws/rules/1000-400.html#fdic1000sec.3a
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A bank, as specified in the Investment Company Act of 1940, is a financial intermediary that is (a) a depository
      institution (as defined in section 3 of the Federal Deposit Insurance Act) or a branch or agency of a foreign bank (as
      such terms are defined in section 1(b) of the International Banking Act of 1978), (b) a member bank of the Federal Reserve
      System, (c) any other banking institution or trust company, whether incorporated or not, doing business under the laws
      of any State or of the United States, a substantial portion of the business of which consists of receiving deposits
      or exercising fiduciary powers similar to those permitted to national banks under the authority of the Comptroller of
      the Currency, and which is supervised and examined by State or Federal authority having supervision over banks, and
      which is not operated for the purpose of evading the provisions of this title, and (d) a receiver, conservator, or other
      liquidating agent of any institution or firm included in clause (a), (b), or (c) of this paragraph.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'The Bank Holding Company Act of 1956 defines a bank as any depository financial intermediary that accepts checking
      accounts (checks) or makes commercial loans, and its deposits are insured by a federal deposit insurance agency. A bank
      acts as a middleman between suppliers of funds and users of funds, substituting its own credit judgement for that of
      the ultimate suppliers of funds, collecting those funds from three sources: checking accounts, savings and time deposits;
      short-term borrowings from other banks; and equity capital. A bank earns money by reinvesting these funds in longer-term
      assets.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.sec.gov/about/laws/ica40.pdf
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/Bank.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/Bank
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/DomesticEntity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/DomesticEntity
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/USBank
sources:
- id: fibo-source-d9bfee9a32
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
  sha256: d9bfee9a3294cc99a3ff7688e325d68a9cc2158ec209ffd10a9a8e411af37f33
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
title: U.S. bank
type: Ontology Class
---

# U.S. bank

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/USBank>

## Definition

bank that is licensed to conduct business in the United States

## Relationships

- **See also**: [ica40.pdf](<https://www.sec.gov/about/laws/ica40.pdf>)
- **Subclass of**: [Bank](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/Bank.md)
- **Subclass of**: [DomesticEntity](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/DomesticEntity.md)

## Annotations

- **label**: U.S. bank
- **definition**: bank that is licensed to conduct business in the United States
- **adaptedFrom**: As defined in the Federal Deposit Insurance Act, https://www.fdic.gov/regulations/laws/rules/1000-400.html#fdic1000sec.3a
- **explanatoryNote**: A bank, as specified in the Investment Company Act of 1940, is a financial intermediary that is (a) a depository institution (as defined in section 3 of the Federal Deposit Insurance Act) or a branch or agency of a foreign bank (as such terms are defined in section 1(b) of the International Banking Act of 1978), (b) a member bank of the Federal Reserve System, (c) any other banking institution or trust company, whether incorporated or not, doing business under the laws of any State or of the United States, a substantial portion of the business of which consists of receiving deposits or exercising fiduciary powers similar to those permitted to national banks under the authority of the Comptroller of the Currency, and which is supervised and examined by State or Federal authority having supervision over banks, and which is not operated for the purpose of evading the provisions of this title, and (d) a receiver, conservator, or other liquidating agent of any institution or firm included in clause (a), (b), or (c) of this paragraph.
- **explanatoryNote**: The Bank Holding Company Act of 1956 defines a bank as any depository financial intermediary that accepts checking accounts (checks) or makes commercial loans, and its deposits are insured by a federal deposit insurance agency. A bank acts as a middleman between suppliers of funds and users of funds, substituting its own credit judgement for that of the ultimate suppliers of funds, collecting those funds from three sources: checking accounts, savings and time deposits; short-term borrowings from other banks; and equity capital. A bank earns money by reinvesting these funds in longer-term assets.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
