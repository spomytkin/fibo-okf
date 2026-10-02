---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: public record
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: record about an action involving a party that is publicly available from a court or other government agency
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This can include court actions such as bankruptcy and foreclosure, as well as liens and other events that have
      been recorded.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/Documents/LegalDocument
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isEvidencedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/PublicRecordCategory
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/Account
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Documents/refersTo
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Documents/Record
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/PublicRecord
sources:
- id: fibo-source-8202fa75b9
  resource: references/fibo/LOAN/LoansGeneral/LoanApplications.rdf
  sha256: 8202fa75b97c33c23b62b818e5df80b122af94dadc7ccf42fe9266d72d61445e
  title: FIBO source LOAN/LoansGeneral/LoanApplications.rdf
title: public record
type: Ontology Class
---

# public record

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/PublicRecord>

## Definition

record about an action involving a party that is publicly available from a court or other government agency

## Relationships

- **Subclass of**: [Record](<https://www.omg.org/spec/Commons/Documents/Record>)

## Constraints

- **[isEvidencedBy](/concepts/fibo/FND/Agreements/Contracts/isEvidencedBy.md)**: min qualified cardinality 0 of type [LegalDocument](<https://www.omg.org/spec/Commons/Documents/LegalDocument>)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: some values from of type [PublicRecordCategory](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/PublicRecordCategory.md)
- **[refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)**: min qualified cardinality 0 of type [Account](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/Account.md)

## Annotations

- **label**: public record
- **definition**: record about an action involving a party that is publicly available from a court or other government agency
- **explanatoryNote**: This can include court actions such as bankruptcy and foreclosure, as well as liens and other events that have been recorded.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
