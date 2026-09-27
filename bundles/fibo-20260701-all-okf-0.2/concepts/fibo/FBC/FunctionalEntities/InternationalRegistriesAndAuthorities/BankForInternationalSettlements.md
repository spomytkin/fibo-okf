---
owl:
  annotations:
  - language: de
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Bank für Internationalen Zahlungsausgleich
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Bank for International Settlements
  - language: fr
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Banque Des Reglements Internationaux
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: international financial organization that serves central banks in their pursuit of monetary and financial stability,
      helping to foster international cooperation in those areas and acting as a bank for central banks
  - language: de
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasLegalName
    value: Bank für Internationalen Zahlungsausgleich
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: BIS
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Office of Financial Research (OFR) Annual Report, 2012, Glossary
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Established in 1930, the BIS is owned by 63 central banks, representing countries from around the world that together
      account for about 95 percent of world GDP. Its head office is in Basel, Switzerland and it has two representative offices:
      in Hong Kong SAR and in Mexico City, as well as Innovation Hub Centres around the world.'
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: https://www.bis.org/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/Instrumentality
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/BankForInternationalSettlementsAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/hasHeadquartersAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/BankForInternationalSettlementsAddress
  - concept: /concepts/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/BankForInternationalSettlementsAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasLegalAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/BankForInternationalSettlementsAddress
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/BankForInternationalSettlements
sources:
- id: fibo-source-d14b800bd9
  resource: references/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities.rdf
  sha256: d14b800bd938a398e868a20a11492151de2fb2a6eb6133acfcd68ecbd3889c65
  title: FIBO source FBC/FunctionalEntities/InternationalRegistriesAndAuthorities.rdf
title: Bank for International Settlements
type: Ontology Individual
---

# Bank for International Settlements

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/BankForInternationalSettlements>

## Definition

international financial organization that serves central banks in their pursuit of monetary and financial stability, helping to foster international cooperation in those areas and acting as a bank for central banks

## Relationships

- **Related to**: [BankForInternationalSettlementsAddress](/concepts/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/BankForInternationalSettlementsAddress.md)
- **Related to**: [BankForInternationalSettlementsAddress](/concepts/fibo/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/BankForInternationalSettlementsAddress.md)

## Annotations

- **label** (de): Bank für Internationalen Zahlungsausgleich
- **label** (en): Bank for International Settlements
- **label** (fr): Banque Des Reglements Internationaux
- **definition**: international financial organization that serves central banks in their pursuit of monetary and financial stability, helping to foster international cooperation in those areas and acting as a bank for central banks
- **hasLegalName** (de): Bank für Internationalen Zahlungsausgleich
- **abbreviation**: BIS
- **adaptedFrom**: Office of Financial Research (OFR) Annual Report, 2012, Glossary
- **explanatoryNote**: Established in 1930, the BIS is owned by 63 central banks, representing countries from around the world that together account for about 95 percent of world GDP. Its head office is in Basel, Switzerland and it has two representative offices: in Hong Kong SAR and in Mexico City, as well as Innovation Hub Centres around the world.
- **hasWebsite**: https://www.bis.org/

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
