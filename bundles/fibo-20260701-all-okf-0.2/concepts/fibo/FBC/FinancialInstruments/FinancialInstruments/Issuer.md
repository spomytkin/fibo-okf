---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: issuer
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: role of a party that issues (or proposes to issue in a formal filing) one or more financial instruments
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Securities Exchange Act of 1934, as amended 12 August 2012
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An issuer can be any legal person, including a legally competent natural person, company, government, or political
      subdivision, agency, or instrumentality of a government, depending on the nature of the instrument. A person might provide
      a loan directly to another party, but most instruments are issued by legal entities.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: With respect to certificates of deposit for securities, voting-trust certificates, or collateral- trust certificates,
      or with respect to certificates of interest or shares in an unincorporated investment trust not having a board of directors
      or of the fixed, restricted management, or unit type, the term issuer means the person or persons performing the acts
      and assuming the duties of depositor or manager pursuant to the provisions of the trust or other agreement or instrument
      under which such securities are issued; and except that with respect to equipment-trust certificates or like securities,
      the term issuer means the person by whom the equipment or property is, or is to be, used.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/issues
    value: N1bda9353896c4769b64f36b06aa219aa
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/hasIssuerShortName
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: N4ae51b06e8ca4d67b87314e16af517aa
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractPrincipal.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractPrincipal
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Issuer
sources:
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
- id: fibo-source-7b3088e831
  resource: references/fibo/SEC/Securities/SecuritiesIssuance.rdf
  sha256: 7b3088e8315beedb43222e345522bb546f87fbbd6850833103c9ba84ea1d7ac0
  title: FIBO source SEC/Securities/SecuritiesIssuance.rdf
title: issuer
type: Ontology Class
---

# issuer

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Issuer>

## Definition

role of a party that issues (or proposes to issue in a formal filing) one or more financial instruments

## Relationships

- **Subclass of**: [ContractPrincipal](/concepts/fibo/FND/Agreements/Contracts/ContractPrincipal.md)

## Constraints

- **[issues](/concepts/fibo/FND/Relations/Relations/issues.md)**: some values from value `N1bda9353896c4769b64f36b06aa219aa`
- **[hasIssuerShortName](/concepts/fibo/SEC/Securities/SecuritiesIssuance/hasIssuerShortName.md)**: min qualified cardinality 0 of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `N4ae51b06e8ca4d67b87314e16af517aa`

## Annotations

- **label**: issuer
- **definition**: role of a party that issues (or proposes to issue in a formal filing) one or more financial instruments
- **adaptedFrom**: Securities Exchange Act of 1934, as amended 12 August 2012
- **explanatoryNote**: An issuer can be any legal person, including a legally competent natural person, company, government, or political subdivision, agency, or instrumentality of a government, depending on the nature of the instrument. A person might provide a loan directly to another party, but most instruments are issued by legal entities.
- **explanatoryNote**: With respect to certificates of deposit for securities, voting-trust certificates, or collateral- trust certificates, or with respect to certificates of interest or shares in an unincorporated investment trust not having a board of directors or of the fixed, restricted management, or unit type, the term issuer means the person or persons performing the acts and assuming the duties of depositor or manager pursuant to the provisions of the trust or other agreement or instrument under which such securities are issued; and except that with respect to equipment-trust certificates or like securities, the term issuer means the person by whom the equipment or property is, or is to be, used.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
