---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: subsidiary of a domestic entity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: entity of which 25 percent or more of whose voting shares are owned or controlled by an entity that is based in
      the United States, or of which a majority of its directors are controlled by such domestic entity, or of which 25 percent
      or more of whose voting shares are held by trustees for the benefit of the shareholders or members of such domestic
      entity
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: From the perspective of the International Banking Act of 1978, the definition of subsidiary is the definition from
      the Bank Holding Act of 1956. Thus, the meaining of the term 'subsidiary' with respect to the NIC repository and, specifically,
      with respect to the definition of an 'international non-bank subsidiary of a domestic entity', is the definition from
      the Bank Holding Company Act of 1956.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The Bank Holding Company Act of 1956 defines a 'Subsidiary', with respect to a specified bank holding company,
      means (1) any company 25 per centum or more of whose voting shares (excluding shares owned by the United States or by
      any company wholly owned by the United States) is owned or controlled by such bank holding company; or (2) any company
      the election of a majority of whose directors is controlled in any manner by such bank holding company; or (3) any company
      25 per centum or more of whose voting shares are held by trustees for the benefit of the shareholders or members of
      such bank holding company.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/isSubsidiaryOf
    value: N59a513de2f7b47218bbb22c36538dc19
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://fraser.stlouisfed.org/title/bank-holding-company-act-1956-984/fulltext
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateControl/Subsidiary.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/Subsidiary
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/SubsidiaryOfADomesticEntity
sources:
- id: fibo-source-d9bfee9a32
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
  sha256: d9bfee9a3294cc99a3ff7688e325d68a9cc2158ec209ffd10a9a8e411af37f33
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
title: subsidiary of a domestic entity
type: Ontology Class
---

# subsidiary of a domestic entity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/SubsidiaryOfADomesticEntity>

## Definition

entity of which 25 percent or more of whose voting shares are owned or controlled by an entity that is based in the United States, or of which a majority of its directors are controlled by such domestic entity, or of which 25 percent or more of whose voting shares are held by trustees for the benefit of the shareholders or members of such domestic entity

## Relationships

- **See also**: [fulltext](<https://fraser.stlouisfed.org/title/bank-holding-company-act-1956-984/fulltext>)
- **Subclass of**: [Subsidiary](/concepts/fibo/BE/OwnershipAndControl/CorporateControl/Subsidiary.md)

## Constraints

- **[isSubsidiaryOf](/concepts/fibo/BE/OwnershipAndControl/CorporateControl/isSubsidiaryOf.md)**: some values from value `N59a513de2f7b47218bbb22c36538dc19`

## Annotations

- **label**: subsidiary of a domestic entity
- **definition**: entity of which 25 percent or more of whose voting shares are owned or controlled by an entity that is based in the United States, or of which a majority of its directors are controlled by such domestic entity, or of which 25 percent or more of whose voting shares are held by trustees for the benefit of the shareholders or members of such domestic entity
- **explanatoryNote**: From the perspective of the International Banking Act of 1978, the definition of subsidiary is the definition from the Bank Holding Act of 1956. Thus, the meaining of the term 'subsidiary' with respect to the NIC repository and, specifically, with respect to the definition of an 'international non-bank subsidiary of a domestic entity', is the definition from the Bank Holding Company Act of 1956.
- **explanatoryNote**: The Bank Holding Company Act of 1956 defines a 'Subsidiary', with respect to a specified bank holding company, means (1) any company 25 per centum or more of whose voting shares (excluding shares owned by the United States or by any company wholly owned by the United States) is owned or controlled by such bank holding company; or (2) any company the election of a majority of whose directors is controlled in any manner by such bank holding company; or (3) any company 25 per centum or more of whose voting shares are held by trustees for the benefit of the shareholders or members of such bank holding company.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
