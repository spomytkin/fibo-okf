---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: registered agent
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: legal agent designated by some party to represent them and act on their behalf under a formal agency agreement
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Agency capacity, as specified in an agency agreement, may include power of attorney, the ability to act as an agent
      in certain kinds of transactions such as real estate, tax, audit or other financial or legal transactions, as a fiduciary,
      including as a trustee or legal guardian, for service of process, and so forth.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: resident agent
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: statutory agent
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: Nd5938045ed464cf981afbc267c72faee
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: http://www.sos.state.tx.us/corp/registeredagents.shtml
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://thelawdictionary.org/agent/
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/LegalAgent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/LegalAgent
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractParty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/RegisteredAgent
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: registered agent
type: Ontology Class
---

# registered agent

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/RegisteredAgent>

## Definition

legal agent designated by some party to represent them and act on their behalf under a formal agency agreement

## Relationships

- **See also**: [registeredagents.shtml](<http://www.sos.state.tx.us/corp/registeredagents.shtml>)
- **See also**: [agent](<https://thelawdictionary.org/agent/>)
- **Subclass of**: [LegalAgent](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/LegalAgent.md)
- **Subclass of**: [ContractParty](/concepts/fibo/FND/Agreements/Contracts/ContractParty.md)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `Nd5938045ed464cf981afbc267c72faee`

## Annotations

- **label**: registered agent
- **definition**: legal agent designated by some party to represent them and act on their behalf under a formal agency agreement
- **explanatoryNote**: Agency capacity, as specified in an agency agreement, may include power of attorney, the ability to act as an agent in certain kinds of transactions such as real estate, tax, audit or other financial or legal transactions, as a fiduciary, including as a trustee or legal guardian, for service of process, and so forth.
- **synonym**: resident agent
- **synonym**: statutory agent

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
