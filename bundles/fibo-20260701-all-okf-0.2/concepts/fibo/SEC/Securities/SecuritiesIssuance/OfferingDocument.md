---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: offering document
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: legal document that states the objectives, risks and terms of an investment
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: EDM Council
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: There are many variations, including offering memorandum, which is typically used in the context of a private placement,
      offering statement, which has slightly different meanings depending on the context (for securities, for bonds, etc.)
      and so forth. This concept is intended to act as a more abstract parent for these more nuanced concepts.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceDocuments/OfferingDocumentTerms
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/SecuritiesOffering
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isEvidenceFor
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/hasExpirationDate
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/DatesAndTimes/hasDateOfIssuance
  subclass_of:
  - concept: /concepts/fibo/BE/FunctionalEntities/Publishers/Publication.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/Publication
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Documents/LegalDocument
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/OfferingDocument
sources:
- id: fibo-source-4c4b98a252
  resource: references/fibo/BP/SecuritiesIssuance/IssuanceDocuments.rdf
  sha256: 4c4b98a25292417c0cfa751a871d67e42ea9e85f29ea26acb47bf9860bbda08e
  title: FIBO source BP/SecuritiesIssuance/IssuanceDocuments.rdf
- id: fibo-source-7b3088e831
  resource: references/fibo/SEC/Securities/SecuritiesIssuance.rdf
  sha256: 7b3088e8315beedb43222e345522bb546f87fbbd6850833103c9ba84ea1d7ac0
  title: FIBO source SEC/Securities/SecuritiesIssuance.rdf
title: offering document
type: Ontology Class
---

# offering document

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/OfferingDocument>

## Definition

legal document that states the objectives, risks and terms of an investment

## Relationships

- **Subclass of**: [Publication](/concepts/fibo/BE/FunctionalEntities/Publishers/Publication.md)
- **Subclass of**: [LegalDocument](<https://www.omg.org/spec/Commons/Documents/LegalDocument>)

## Constraints

- **[hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)**: some values from of type [OfferingDocumentTerms](/concepts/fibo/BP/SecuritiesIssuance/IssuanceDocuments/OfferingDocumentTerms.md)
- **[isEvidenceFor](/concepts/fibo/FND/Agreements/Contracts/isEvidenceFor.md)**: exact qualified cardinality 1 of type [SecuritiesOffering](/concepts/fibo/SEC/Securities/SecuritiesIssuance/SecuritiesOffering.md)
- **[hasExpirationDate](/concepts/fibo/FND/Arrangements/Documents/hasExpirationDate.md)**: exact qualified cardinality 1 of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)
- **[hasDateOfIssuance](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDateOfIssuance>)**: exact qualified cardinality 1 of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)

## Annotations

- **label**: offering document
- **definition**: legal document that states the objectives, risks and terms of an investment
- **adaptedFrom**: EDM Council
- **explanatoryNote**: There are many variations, including offering memorandum, which is typically used in the context of a private placement, offering statement, which has slightly different meanings depending on the context (for securities, for bonds, etc.) and so forth. This concept is intended to act as a more abstract parent for these more nuanced concepts.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
