---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit facility debt basket
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: basket of securities whose constituents are credit agreements that allow the borrower to periodically take out
      money over an extended period of time rather than reapplying for a loan every time they need funds
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The credit facility debt basket consists of a number of credit facilities including revolving loans/line of credit,
      committed facilities, letters of credit and most retail credit accounts. The first port of call for issuers is the credit
      facility debt basket. In addition to the fixed dollar (or euro) amounts, credit facility debt baskets in senior secured
      notes and indentures typically provide for a grower component that is the greater of the fixed dollar/euro amount and
      a percentage of total assets, total tangible assets or EBITDA.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
    value: N79eccbfb82bc4635985fb69dce4e7c88
  subclass_of:
  - concept: /concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/BasketOfDebtInstruments.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/BasketOfDebtInstruments
resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/CreditFacilityDebtBasket
sources:
- id: fibo-source-e409c614fa
  resource: references/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives.rdf
  sha256: e409c614fa05cf3a92ef2ffb652008525612be13fc2347acd6b082fe0f4dc330
  title: FIBO source DER/SecurityBasedDerivatives/SecurityBasedDerivatives.rdf
title: credit facility debt basket
type: Ontology Class
---

# credit facility debt basket

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/CreditFacilityDebtBasket>

## Definition

basket of securities whose constituents are credit agreements that allow the borrower to periodically take out money over an extended period of time rather than reapplying for a loan every time they need funds

## Relationships

- **Subclass of**: [BasketOfDebtInstruments](/concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/BasketOfDebtInstruments.md)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from value `N79eccbfb82bc4635985fb69dce4e7c88`

## Annotations

- **label** (en): credit facility debt basket
- **definition** (en): basket of securities whose constituents are credit agreements that allow the borrower to periodically take out money over an extended period of time rather than reapplying for a loan every time they need funds
- **explanatoryNote** (en): The credit facility debt basket consists of a number of credit facilities including revolving loans/line of credit, committed facilities, letters of credit and most retail credit accounts. The first port of call for issuers is the credit facility debt basket. In addition to the fixed dollar (or euro) amounts, credit facility debt baskets in senior secured notes and indentures typically provide for a grower component that is the greater of the fixed dollar/euro amount and a percentage of total assets, total tangible assets or EBITDA.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
